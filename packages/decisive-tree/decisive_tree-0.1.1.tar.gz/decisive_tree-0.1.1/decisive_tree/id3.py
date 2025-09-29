from treelib import Tree
from .node_data import NodeData
from typing import List
import pandas as pd
import numpy as np

class ID3:
    def __init__(self):
        self._tree = None
        self._classes = None

    def plot(self):
        self._tree.show(data_property="tostr")

    def fit(self, X: pd.DataFrame, y: pd.DataFrame):
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
            value = sample[feature]
            next_node = None

            for child in self._tree.children(cur_node.identifier):
                if child.tag == value:
                    next_node = child
                    break

            if next_node == None:
                return cur_node.data.majority_prediction
            
            cur_node = next_node
        
        return cur_node.data.prediction


    def _build_tree(self, X: pd.DataFrame, y: pd.Series, cur_id: str, branch=None):
        samples_count = len(y)
        samples_per_class = y.value_counts().reindex(self._classes, fill_value=0).tolist()
        
        majority_class = y.mode()[0]

        if len(y.unique()) == 1:
            prediction = y.iloc[0]
            self._tree.get_node(cur_id).data = NodeData(True, samples_count, *samples_per_class, branch=branch, prediction=prediction, majority_prediction=majority_class)
            return

        if len(X.columns) == 0:
            majority_class = y.mode()[0]
            self._tree.get_node(cur_id).data = NodeData(True, samples_count, *samples_per_class, branch=branch, prediction=majority_class, majority_prediction=majority_class)
            return

        gains = { c: self._gain(X[c], y) for c in X.columns }
        best_feature = max(gains, key=gains.get)
        
        self._tree.get_node(cur_id).data = NodeData(False, samples_count, *samples_per_class, branch=branch, feature=best_feature, majority_prediction=majority_class)

        for value in X[best_feature].unique():
            child_id = f"{cur_id}_{value}"
            self._tree.create_node(tag=str(value), identifier=child_id, parent=cur_id)

            subset_indices = X[X[best_feature] == value].index
            new_X = X.loc[subset_indices].drop(columns=[best_feature])
            new_y = y.loc[subset_indices]

            self._build_tree(new_X, new_y, child_id, branch=value)
            
    def _gain(self, attr: pd.Series, y: pd.DataFrame) -> float:
        s = 0
        freqs = attr.value_counts(normalize=True)
        for k in freqs.index:
            filtered = y[attr == k]
            s += freqs[k] * self._entropy(filtered)
        return self._entropy(y) - s
    
    def _entropy(self, data: pd.Series) -> float:
        return np.sum((-pi * np.log2(pi)) for pi in data.value_counts(normalize=True))