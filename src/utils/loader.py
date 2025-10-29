import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple, List


def load_pima(path: str) -> Tuple[pd.DataFrame, List[int]]:
    df = pd.read_csv(path)
    if "Outcome" not in df.columns:
        raise ValueError("Expected 'Outcome' column in CSV.")

    X = df.drop(columns=["Outcome"])
    y = df["Outcome"].astype(int).tolist()
    return X, y


def train_test(
    path: str,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, List[int], List[int]]:
    X, y = load_pima(path)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train.reset_index(drop=True), X_test.reset_index(drop=True), y_train, y_test

# if __name__ == "__main__":
#     X_train, X_test, y_train, y_test = train_test("data/pima.csv")
#     print("Train shape:", X_train.shape)
#     print("Test shape:", X_test.shape)
#     print("First sample:", X_train.iloc[0].to_dict(), "→", y_train[0])
