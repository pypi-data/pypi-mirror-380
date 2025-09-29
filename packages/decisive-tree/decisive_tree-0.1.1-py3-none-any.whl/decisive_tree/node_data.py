class NodeData:
    def __init__(
            self, 
            is_leaf: bool, 
            samples: int, 
            *samples_values: int, 
            branch=None, 
            prediction=None, 
            majority_prediction=None,
            feature=None, 
            threshold=None):
        self.is_leaf = is_leaf
        self.branch = branch
        self.prediction = prediction
        self.majority_prediction = majority_prediction
        self.feature = feature
        self.threshold = threshold
        self.tostr = ""
        if branch is not None:
            self.tostr += f"{branch}: "
        if self.is_leaf:
            self.tostr += f"Predict({self.prediction})"
        else:
            self.tostr += f"Split({self.feature}"
            if threshold is not None:
                self.tostr += f", {threshold}"
            self.tostr += ")"
        self.tostr += f", samples={samples}, samples_values={samples_values}"