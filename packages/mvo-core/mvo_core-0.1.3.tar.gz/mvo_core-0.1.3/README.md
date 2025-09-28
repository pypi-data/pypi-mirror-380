markdown
# my_mvo

A Python package for **Mortality Vector Optimization (MVO)** to predict patient outcomes using multi-stage vector optimization.

## Features

- **Feature Normalization**: Robust preprocessing of feature matrices
- **Multi-stage Optimization**: Sequential vector optimization for improved prediction accuracy
- **Comprehensive Evaluation**: Bootstrap-based assessment with multiple metrics:
  - AUC (Area Under the ROC Curve)
  - Brier Score
  - C-index (Concordance Index)
- **Probability Prediction**: Logistic regression-based outcome probability estimation
- **Modular Design**: Flexible components for custom pipeline integration

## Installation

```bash
pip install mvo-core