import pandas as pd
import os
# from sklearn.model_selection import train_test_split
# from typing import Tuple, List


# def load_pima(path: str) -> Tuple[pd.DataFrame, List[int]]:
#     df = pd.read_csv(path)
#     if "Outcome" not in df.columns:
#         raise ValueError("Expected 'Outcome' column in CSV.")

#     X = df.drop(columns=["Outcome"])
#     y = df["Outcome"].astype(int).tolist()
#     return X, y


# def train_test(
#     path: str,
#     test_size: float = 0.2,
#     random_state: int = 42,
# ) -> Tuple[pd.DataFrame, pd.DataFrame, List[int], List[int]]:
#     X, y = load_pima(path)
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, test_size=test_size, random_state=random_state, stratify=y
#     )
#     return X_train.reset_index(drop=True), X_test.reset_index(drop=True), y_train, y_test

# if __name__ == "__main__":
#     X_train, X_test, y_train, y_test = train_test("data/pima.csv")
#     print("Train shape:", X_train.shape)
#     print("Test shape:", X_test.shape)
#     print("First sample:", X_train.iloc[0].to_dict(), "→", y_train[0])

#https://docs.python.org/3/reference/compound_stmts.html#function-definitions
"""
funcdef:             
[decorators] "def" funcname [type_params] "(" [parameter_list] ")"
["->" expression] ":" suite

def                ← keyword
load_csv           ← funcname
(path: str)        ← parameter_list
-> pd.DataFrame    ← return annotation (expression)
:                  ← header terminator
suite              ← indented block (body)
"""

# path = "data/Iris.csv"

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

# c = load_csv(path)
# d=c.drop(columns =('Species'))
# print(c)
# x = c.drop(columns=(["Species","Id"]))
# print(x)
# y = c["Species"]
# print(y)
# print(type(y))
# print("")
# print(y.iloc[0])
# print(y[0])
# print(y.unique())
# print()
# print(d)
# e = c.drop(columns= ['Id', 'Species'])
# print(e)
# print(c.index.values)
# print(c.columns)
# print(c.columns.values)
# print(os.getcwd())
# print(type(c))