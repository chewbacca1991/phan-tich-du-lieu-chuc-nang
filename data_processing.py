import pandas as pd

class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        # Logic để tải dữ liệu
        return pd.read_csv(self.data_source)

    def clean_data(self, df):
        # Logic để làm sạch dữ liệu
        return df.dropna()