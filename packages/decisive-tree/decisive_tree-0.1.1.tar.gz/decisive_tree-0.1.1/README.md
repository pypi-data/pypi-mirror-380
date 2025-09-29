# Decisive Tree

[![PyPI Version](https://img.shields.io/pypi/v/decisive-tree.svg)](https://pypi.org/project/decisive-tree/)
[![Python Version](https://img.shields.io/pypi/pyversions/decisive-tree.svg)](https://pypi.org/project/decisive-tree/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/mateushmd/decisive-tree/publish.yml)](https://github.com/mateushmd/decisive-tree/actions)

A from-scratch Python implementation of the ID3, C4.5, and CART decision tree algorithms, created for educational purposes.

This project provides a clear and understandable look into the core mechanics of these foundational machine learning models, from the splitting criteria to the recursive tree-building process. It also includes a suite of from-scratch utilities for data preprocessing and model evaluation.

## Key Features

* **ID3 Algorithm**: Implements the classic algorithm using Information Gain, perfect for datasets with nominal features.
* **C4.5 Algorithm**: An extension of ID3 using Gain Ratio to handle both nominal (multi-way split) and continuous features (binary split).
* **CART Algorithm**: Implements Classification and Regression Trees using Gini Impurity (for classification) and Variance Reduction (for regression) with strictly binary splits for all feature types.
* **Utilities**: Includes custom, understandable implementations of:
    * Data splitting and preprocessing (`split_data`, `one_hot_encode`, `ordinal_encode`).
    * Model evaluation (`get_confusion_matrix`, `calculate_metrics`, `plot_confusion_matrix`).
* **Tree Visualization**: All models include a `.plot()` method for a simple console-based visualization of the resulting tree structure.

---

## Installation

You can install `decisive-tree` directly from PyPI:

```sh
pip install decisive-tree