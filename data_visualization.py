import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data)
        plt.title('Data Visualization Over Time')  # More descriptive title
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.show()