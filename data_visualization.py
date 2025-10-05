import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data)
        plt.title('Dữ liệu phân tích')
        plt.xlabel('Thời gian')
        plt.ylabel('Giá trị')
        plt.show()