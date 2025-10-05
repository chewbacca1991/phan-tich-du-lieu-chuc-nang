from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

class MLModel:
    def __init__(self, data):
        self.data = data
        self.model = LinearRegression()

    def train(self):
        X = self.data.drop('target', axis=1)
        y = self.data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)

    def validate(self, new_data):
        if 'target' not in new_data.columns:
            raise ValueError("new_data must contain 'target' column.")
        X_new = new_data.drop('target', axis=1)
        y_new = new_data['target']
        return self.model.score(X_new, y_new)