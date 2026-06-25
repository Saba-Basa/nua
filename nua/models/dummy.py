from nua.base.classifier import Classifier


class DummyClassifier(Classifier):
    def fit(self, X, y):
        self.label = 0

    def predict(self, X):
        return [self.label] * len(X)