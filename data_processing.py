import pandas as pd

class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        # Logic to load data
        return pd.read_csv(self.data_source)

    def clean_data(self, df):
        # Logic to clean data
        return df.dropna()