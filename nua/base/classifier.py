from abc import ABC, abstractmethod
"""
Base classifier (estimator).

Mathematical model:
    θ̂ = f(X, y)     # fit step (parameter estimation)
    ŷ = g(X; θ̂)     # predict step (inference)

An estimator learns parameters θ̂ from data (fit),
and a classifier predicts discrete labels ŷ for new samples (predict).
"""

class Classifier(ABC):
    #learn from examples
    
    @abstractmethod
    def fit(self, X, y):
        """
        Learn model parameters θ̂ from training data.
        Mathematically:
            θ̂ = f(X, y)
        where:
            X — input features
            y — target labels
            f — learning algorithm estimating parameters that best explain y given X
        """
        pass
    
    
    #apply what was learned
    
    @abstractmethod
    def predict(self, X):
        """
        Infer outputs ŷ for new inputs using learned parameters θ̂.

        Mathematically:
            ŷ = g(X; θ̂)
        where:
            X — new input features
            θ̂ — parameters estimated during fit()
            g — decision rule or inference function
        """
        pass