"""
Validation utilities for TOPSIS inputs.
"""

import os
import pandas as pd


def validate_file(path):
    if not os.path.isfile(path):
        raise FileNotFoundError("Input file does not exist")


def load_and_validate_csv(path):
    df = pd.read_csv(path)

    if df.shape[1] < 3:
        raise ValueError("Input file must contain at least 3 columns")

    criteria = df.iloc[:, 1:]

    if not criteria.applymap(lambda x: isinstance(x, (int, float))).all().all():
        raise ValueError("All criteria values must be numeric")

    return df


def parse_weights(weights_str, n_criteria):
    try:
        weights = list(map(float, weights_str.split(",")))
    except ValueError:
        raise ValueError("Weights must be numeric and comma-separated")

    if len(weights) != n_criteria:
        raise ValueError("Number of weights must match number of criteria")

    return weights


def parse_impacts(impacts_str, n_criteria):
    impacts = impacts_str.split(",")

    if len(impacts) != n_criteria:
        raise ValueError("Number of impacts must match number of criteria")

    for i in impacts:
        if i not in ["+", "-"]:
            raise ValueError("Impacts must be either '+' or '-'")

    return impacts
