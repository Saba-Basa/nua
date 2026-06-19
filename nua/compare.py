from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from utils.loader import train_test
from utils.discretize import fit_quantile_bins, transform_with_bins
from id3 import ID3  # adjust import if your class is in models/

def main():
    # 1) Load & split
    X_train, X_test, y_train, y_test = train_test("data/pima.csv")

    # 2) Discretize for ID3 (and fair compare)
    edges = fit_quantile_bins(X_train, n_bins=4)
    Xtr_disc = transform_with_bins(X_train, edges)
    Xte_disc = transform_with_bins(X_test, edges)

    # 3) ID3 expects list[dict]
    train_dicts = [row.to_dict() for _, row in Xtr_disc.iterrows()]
    test_dicts  = [row.to_dict() for _, row in Xte_disc.iterrows()]
    dataset = [{**d, "__label__": y} for d, y in zip(train_dicts, y_train)]
    attrs = list(Xtr_disc.columns)

    # 4) Train & eval ID3
    id3 = ID3().fit(dataset, attrs, "__label__")
    y_pred_id3 = id3.predict(test_dicts)
    print("ID3 (discretized) accuracy:", accuracy_score(y_test, y_pred_id3))

    # 5) Sklearn tree on same discretized features (fair apples-to-apples)
    dt_disc = DecisionTreeClassifier(criterion="entropy", random_state=42)
    dt_disc.fit(Xtr_disc.values, y_train)
    y_pred_dt_disc = dt_disc.predict(Xte_disc.values)
    print("sklearn DecisionTree (discretized) accuracy:", accuracy_score(y_test, y_pred_dt_disc))

    # 6) Sklearn tree on raw features (baseline)
    dt_raw = DecisionTreeClassifier(criterion="entropy", random_state=42)
    dt_raw.fit(X_train.values, y_train)
    y_pred_dt_raw = dt_raw.predict(X_test.values)
    print("sklearn DecisionTree (raw) accuracy:", accuracy_score(y_test, y_pred_dt_raw))

if __name__ == "__main__":
    main()
