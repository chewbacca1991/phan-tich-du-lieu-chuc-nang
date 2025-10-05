import pandas as pd

class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        """Load data from the specified source."""
        return pd.read_csv(self.data_source)

    def clean_data(self, df, reset_index=False):
        """Clean the DataFrame by dropping rows with missing values. Optionally reset index."""
        df_cleaned = df.dropna()
        return df_cleaned.reset_index(drop=True) if reset_index else df_cleaned