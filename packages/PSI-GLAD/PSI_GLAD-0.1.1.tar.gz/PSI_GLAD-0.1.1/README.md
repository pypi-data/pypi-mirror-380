# Post-Selection Inference for Generalized Lasso after Optimal Transport-based Domain Adaptation

[![PyPI version](https://img.shields.io/pypi/v/psi-glad)](https://img.shields.io/pypi/v/psi-glad)
![License](https://img.shields.io/github/license/DAIR-Group/PSI-GLAD)

PSI-GLAD is a Python package that implements a selective inference (SI) framework for conducting valid statistical inference after generalized lasso (GL) in the presence of domain adaptation (DA). The main idea is to leverages the SI framework and employs a divide-and conquer approach to efficiently compute the $p$ -value. Our proposed methods provides valid $p$-value for GL-DA results, by keeping the false positive rate (FPR) under control, while also maximizing the true positive rate (TPR), i.e., lowering the false negative rate (FNR).

## Requirements
This package has the following requirements:

    cvxpy
    mpmath
    numpy
    POT
    scikit-learn
    scipy

## Installation

### Package Installation
This package can be installed using pip:
```bash
$ pip install psi_glad
```

## Usage

We provide several Jupyter notebooks demonstrating how to use the stand-da package in action.

- Examples for conducting inference for Feature Selection/Change Point Detection-based Generalized Lasso after OT-based DA
```
>> ex1_feature_selection_after_DA.ipynb
```
```
>> ex2_change_point_detection_after_DA.ipynb
```
- Check the uniformity of the pivot
```
>> ex3_validity_of_p_value.ipynb
```