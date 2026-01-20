import pandas as pd
# split by x and y
# return X, y

"""
What is being implemented?
- A function that splits a dataset into model inputs and targets.

What is this unit?
- Schema splitter function (feature/target separation).

What SINGLE job does it perform?
- Splits a raw DataFrame into feature matrix X and target vector y.

When is this executed?
=========
PIPELINE:
    1 Load data
    2 Schema split (X / y separation)
    3 Cleaning (impute, scale, encode)
    4 Train model
=========
- Executed after data loading to define modeling inputs and targets.

Why must this exist as its own unit?
- Schema splitting is isolated so that changing column names or roles only requires changing ONE place in the code.

Example:
Before: target = "Species"
After:  target = "FlowerType"

Schema function logic stays fixed.
Only the target parameter changes.

Rule:
One structural change → one code location.

What must it NOT handle?
- Data cleaning (missing values, scaling, encoding).

"""

def split_xy(df : pd.DataFrame, target: str,drop: list[str] = None):
    
    return 0