from typing import List, Dict, Any, Tuple
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_confusion_matrix(y_true: pd.Series, y_pred: List[Any]) -> tuple[np.array, list]:
    class_labels = sorted(list(set(y_true) | set(y_pred)))
    class_to_idx = {label: i for i, label in enumerate(class_labels)}

    num_classes = len(class_labels)
    matrix = np.zeros((num_classes, num_classes), dtype=int)

    for true_label, pred_label in zip(y_true, y_pred):
        true_idx = class_to_idx[true_label]
        pred_idx = class_to_idx[pred_label]
        matrix[true_idx, pred_idx] += 1

    return matrix, class_labels

def plot_confusion_matrix(y_true: pd.Series, y_pred: List[Any]):
    matrix, class_labels = get_confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
    plt.xlabel('Predict Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

def calculate_metrics(y_true: pd.Series, y_pred: List[Any]):
    matrix, class_labels = get_confusion_matrix(y_true, y_pred)
    num_classes = len(class_labels)
    metrics = {}

    metrics['accuracy'] = np.trace(matrix) / np.sum(matrix)

    per_class_precision = []
    per_class_recall = []
    per_class_f1 = []

    for i, label in enumerate(class_labels):
        tp = matrix[i, i]
        fp = np.sum(matrix[:, i]) - tp
        fn = np.sum(matrix[i, :]) - tp

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        metrics[f'{label}_precision'] = precision
        per_class_precision.append(precision)

        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        metrics[f'{label}_recall'] = recall
        per_class_recall.append(recall)
        
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        metrics[f'{label}_f1_score'] = f1
        per_class_f1.append(f1)

    metrics['macro_precision'] = np.mean(per_class_precision)
    metrics['macro_recall'] = np.mean(per_class_recall)
    metrics['macro_f1_score'] = np.mean(per_class_f1)
    
    return metrics