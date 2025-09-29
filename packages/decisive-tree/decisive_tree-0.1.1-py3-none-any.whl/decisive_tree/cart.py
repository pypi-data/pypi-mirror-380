from treelib import Tree
from .node_data import NodeData
import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
from typing import List, Tuple, Any
from itertools import chain, combinations

class CART:
    def __init__(self, mode='classification', min_samples_leaf=1, max_depth=10):
        if mode not in ['classification', 'regression']:
            raise ValueError("mode must be 'classification' or 'regression'")
        self._tree = None
        self._classes = None
        self._mode = mode
        self._min_samples_leaf = min_samples_leaf
        self._max_depth = max_depth

    def plot(self):
        self._tree.show(data_property="tostr")

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self._tree = Tree()
        if self._mode == 'classification':
            self._classes = y.unique()
        self._tree.create_node(tag="Root", identifier="root")
        self._build_tree(X, y, "root", depth=0)
        return self
    
    def predict(self, X: pd.DataFrame) -> List[str]:
        return [self._predict(row) for _, row in X.iterrows()]
    
    def _predict(self, sample: pd.Series) -> str:
        cur_node = self._tree.get_node(self._tree.root)

        while not cur_node.data.is_leaf:
            feature = cur_node.data.feature
            threshold = cur_node.data.threshold
            value = sample[feature]
            children = self._tree.children(cur_node.identifier)

            if isinstance(threshold, list):
                cur_node = children[0] if value in threshold else children[1]
            else:
                cur_node = children[0] if value <= threshold else children[1]
        
        return cur_node.data.prediction

    def _build_tree(self, X: pd.DataFrame, y: pd.Series, parent_id: str, depth: int, branch=None):
        samples_count = len(y)
        samples_per_class = y.value_counts().reindex(self._classes, fill_value=0).tolist() if self._mode == 'classification' else [0]
        
        if depth >= self._max_depth or samples_count < self._min_samples_leaf or len(y.unique()) == 1:
            leaf_value = y.mode()[0] if self._mode == 'classification' else y.mean()
            self._tree.get_node(parent_id).data = NodeData(True, samples_count, *samples_per_class, branch=branch, prediction=leaf_value)
            return

        best_feature, best_threshold = self._find_best_split(X, y)
        
        if best_feature is None:
            leaf_value = y.mode()[0] if self._mode == 'classification' else y.mean()
            self._tree.get_node(parent_id).data = NodeData(True, samples_count, *samples_per_class, branch=branch, prediction=leaf_value)
            return

        node_data = NodeData(False, samples_count, *samples_per_class, branch=branch, feature=best_feature, threshold=best_threshold)
        self._tree.get_node(parent_id).data = node_data
        
        if is_numeric_dtype(X[best_feature]):
            left_mask = X[best_feature] <= best_threshold
            branch_left_tag = f"<= {best_threshold:.2f}"
            branch_right_tag = f"> {best_threshold:.2f}"
        else:
            left_mask = X[best_feature].isin(best_threshold)
            branch_left_tag = f"in {best_threshold}"
            branch_right_tag = f"not in {best_threshold}"
        right_mask = ~left_mask
        
        left_id = f"{parent_id}_L"
        self._tree.create_node(tag=branch_left_tag, identifier=left_id, parent=parent_id)
        self._build_tree(X[left_mask], y[left_mask], left_id, depth + 1, branch=branch_left_tag)

        right_id = f"{parent_id}_R"
        self._tree.create_node(tag=branch_right_tag, identifier=right_id, parent=parent_id)
        self._build_tree(X[right_mask], y[right_mask], right_id, depth + 1, branch=branch_right_tag)

    def _find_best_split(self, X: pd.DataFrame, y: pd.Series) -> Tuple[str, Any]:
        best_score = -1
        best_feature = None
        best_threshold = None
        parent_impurity = self._get_impurity(y)

        for feature in X.columns:
            unique_values = X[feature].unique()
            
            if is_numeric_dtype(X[feature]):
                for i in range(len(unique_values) - 1):
                    threshold = (unique_values[i] + unique_values[i+1]) / 2
                    left_mask = X[feature] <= threshold
                    right_mask = X[feature] > threshold
                    
                    y_left, y_right = y[left_mask], y[right_mask]
                    if len(y_left) == 0 or len(y_right) == 0: continue

                    w_left, w_right = len(y_left) / len(y), len(y_right) / len(y)
                    weighted_impurity = w_left * self._get_impurity(y_left) + w_right * self._get_impurity(y_right)
                    score = parent_impurity - weighted_impurity

                    if score > best_score:
                        best_score, best_feature, best_threshold = score, feature, threshold
            else:
                powerset = list(chain.from_iterable(combinations(unique_values, r) for r in range(1, len(unique_values))))
                for subset in powerset:
                    threshold = list(subset)
                    left_mask = X[feature].isin(threshold)
                    right_mask = ~left_mask

                    y_left, y_right = y[left_mask], y[right_mask]
                    if len(y_left) == 0 or len(y_right) == 0: continue
                    
                    w_left, w_right = len(y_left) / len(y), len(y_right) / len(y)
                    weighted_impurity = w_left * self._get_impurity(y_left) + w_right * self._get_impurity(y_right)
                    score = parent_impurity - weighted_impurity

                    if score > best_score:
                        best_score, best_feature, best_threshold = score, feature, threshold

        if best_score <= 0:
            return None, None

        return best_feature, best_threshold

    def _gini_impurity(self, y: pd.Series) -> float:
        if y.empty: return 0
        probs = y.value_counts(normalize=True)
        return 1 - np.sum(probs**2)

    def _variance(self, y: pd.Series) -> float:
        if y.empty: return 0
        return y.var()

    def _get_impurity(self, y: pd.Series) -> float:
        if self._mode == 'classification':
            return self._gini_impurity(y)
        else:
            return self._variance(y)    