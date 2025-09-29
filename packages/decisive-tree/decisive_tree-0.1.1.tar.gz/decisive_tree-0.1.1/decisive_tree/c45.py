from treelib import Tree
from .node_data import NodeData
from pandas.api.types import is_numeric_dtype
from typing import List, Tuple
import pandas as pd
import numpy as np

class C45:
    def __init__(self):
        self._tree = None
        self._classes = None
    
    def plot(self):
        self._tree.show(data_property="tostr")

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self._tree = Tree()
        self._classes = y.unique()
        self._tree.create_node(tag="Root", identifier="root")
        self._build_tree(X, y, "root")
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
            next_node = None

            if threshold != None:
                next_node = children[0] if value <= threshold else children[1]
            else:
                for child in children:
                    if child.tag == value:
                        next_node = child
                        break

            if next_node == None:
                return cur_node.data.majority_prediction
            
            cur_node = next_node
        
        return cur_node.data.prediction

    def _build_tree(self, X: pd.DataFrame, y: pd.Series, parent_id: str, branch=None):
        samples_count = len(y)
        samples_per_class = y.value_counts().reindex(self._classes, fill_value=0).tolist()

        majority_class = y.mode()[0]

        if len(y.unique()) == 1:
            prediction = y.iloc[0]
            self._tree.get_node(parent_id).data = NodeData(True, samples_count, *samples_per_class, branch=branch, prediction=prediction, majority_prediction=majority_class)
            return

        if len(X.columns) == 0:
            majority_class = y.mode()[0]
            self._tree.get_node(parent_id).data = NodeData(True, samples_count, *samples_per_class, branch=branch, prediction=majority_class, majority_prediction=majority_class)
            return
        
        best_feature, split_point = self._best_split(X, y)

        if best_feature is None:
            majority_class = y.mode()[0]
            self._tree.get_node(parent_id).data = NodeData(True, samples_count, *samples_per_class, branch=branch, prediction=majority_class, majority_prediction=majority_class)
            return

        node_data = NodeData(False, samples_count, *samples_per_class, branch=branch, feature=best_feature, threshold=split_point, majority_prediction=majority_class)
        self._tree.get_node(parent_id).data = node_data

        if split_point is None:
            for value in X[best_feature].unique():
                child_id = f"{parent_id}_{value}"
                self._tree.create_node(tag=str(value), identifier=child_id, parent=parent_id)

                subset_indices = X[X[best_feature] == value].index

                new_X = X.loc[subset_indices].drop(columns=[best_feature])
                new_y = y.loc[subset_indices]
                
                self._build_tree(new_X, new_y, child_id, branch=value)
        else:
            left_mask = X[best_feature] <= split_point
            left_id = f"{parent_id}_<={split_point}"
            self._tree.create_node(tag=f"<= {split_point}", identifier=left_id, parent=parent_id)
            
            new_X_left = X[left_mask]
            new_y_left = y[left_mask]
            self._build_tree(new_X_left, new_y_left, left_id, branch=f"<= {split_point}")

            right_mask = X[best_feature] > split_point
            right_id = f"{parent_id}_>{split_point}"
            self._tree.create_node(tag=f"> {split_point}", identifier=right_id, parent=parent_id)
            
            new_X_right = X[right_mask]
            new_y_right = y[right_mask]
            self._build_tree(new_X_right, new_y_right, right_id, branch=f"> {split_point}")

    def _best_split(self, X: pd.DataFrame, y: pd.Series) -> Tuple[str, float]:
        best_gain_ratio = -1
        best_feature = None
        best_split_point = None

        for name, series in X.items():
            if is_numeric_dtype(series):
                gain_ratio, split_point = self._find_best_binary_split(series, y)
            else:
                _, _, gain_ratio = self._calculate_gain_ratio(series, y)
                split_point = None

            if gain_ratio > best_gain_ratio:
                best_gain_ratio = gain_ratio
                best_feature = name
                best_split_point = split_point
        
        if best_gain_ratio <= 0:
            return None, None
            
        return best_feature, best_split_point

    def _find_best_binary_split(self, feature: pd.Series, y: pd.Series) -> Tuple[float, float]:
        best_gain_ratio = -1
        best_split_point = None
        unique_values = feature.unique()
        unique_values.sort()

        for i in range(len(unique_values) - 1):
            split_point = (unique_values[i] + unique_values[i+1]) / 2
            left_mask = feature <= split_point
            right_mask = feature > split_point
            y_left = y[left_mask]
            y_right = y[right_mask]

            if len(y_left) == 0 or len(y_right) == 0:
                continue

            parent_entropy = self._entropy(y)
            weight_left = len(y_left) / len(y)
            weight_right = len(y_right) / len(y)
            weighted_child_entropy = (weight_left * self._entropy(y_left)) + (weight_right * self._entropy(y_right))
            information_gain = parent_entropy - weighted_child_entropy
            
            if weight_left == 0 or weight_right == 0:
                 split_info = 0
            else:
                 split_info = -weight_left * np.log2(weight_left) - weight_right * np.log2(weight_right)

            gain_ratio = 0 if split_info == 0 else information_gain / split_info
                
            if gain_ratio > best_gain_ratio:
                best_gain_ratio = gain_ratio
                best_split_point = split_point

        return best_gain_ratio, best_split_point
    
    def _calculate_gain_ratio(self, feature: pd.Series, y: pd.Series) -> Tuple[float, float, float]:
        freqs = feature.value_counts(normalize=True)
        parent_entropy = self._entropy(y)
        weighted_child_entropy = 0
        split_info = 0
        
        for k, freq in freqs.items():
            filtered_y = y[feature == k]
            weighted_child_entropy += freq * self._entropy(filtered_y)
            if freq > 0:
                split_info -= freq * np.log2(freq)

        information_gain = parent_entropy - weighted_child_entropy
        gain_ratio = 0 if split_info == 0 else information_gain / split_info
        
        return information_gain, split_info, gain_ratio
    
    def _entropy(self, data: pd.Series) -> float:
        probs = data.value_counts(normalize=True)
        return -np.sum([p * np.log2(p) for p in probs if p > 0])