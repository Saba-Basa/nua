from xgboost import XGBClassifier

class XGBoostClassifier:
    def __init__(self):
        self.model = XGBClassifier()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)