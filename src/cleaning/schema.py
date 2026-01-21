import pandas as pd
# split by x and y
# return X, y

"""
What is being implemented?
- A function that splits a dataset into model inputs and targets.

=========
Operation = split dataset into X and y
Name = split_xy
Type = function
=========

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

Isolate Unit

A function that splits a dataset into model inputs and targets.

A)
splits a dataset into model inputs and targets.
B)
Split dataset
C)
Split table
D)
Table split

INPUT 
What is the input name?
table

What role does it play?
Primary data

What structure is it?
Table

What is its concrete type?
Table / Matrix type - pandas.DataFrame

Who owns this data?
Caller-owned 

OUTPUT
What is the output name?
X

What role does it play?
Primary result 

What structure is it?
Table - DataFrame

What is its concrete type?
pandas.DataFrame

OUTPUT
What is the output name?
y

What role does it play?
Primary result 

What structure is it?
Collection -> pandas.Series, labled vector

How many outputs are produced?
Multiple -> table, collection

Does this unit change anything OUTSIDE its main output artifacts?
None

"""

def split_xy(df : pd.DataFrame, target: str,drop: list[str] = None)-> tuple[pd.DataFrame,pd.Series]:
    
    #---- input validation ----
    #typecheck validation
    #empty
    #target error
    #typeError
    #keyerror
    #drop error
    
    # --- split ----
    
    # extract y
    # build X
    #drop columns
    
    raise NotImplementedError("split_xy not implemented yet")
