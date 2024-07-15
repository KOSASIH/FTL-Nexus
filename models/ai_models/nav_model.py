import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class NavModel:
    def __init__(self, training_data):
        self.training_data = training_data
        self.model = RandomForestClassifier()

    def train(self):
        self.model.fit(self.training_data.drop("target", axis=1), self.training_data["target"])

    def predict(self, input_data):
        return self.model.predict(input_data)
