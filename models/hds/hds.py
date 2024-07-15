import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class HDS:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def display_hologram(self, data):
        # Display the hologram using matplotlib
        self.ax.scatter(data[:, 0], data[:, 1], data[:, 2])
        plt.show()

data = np.random.rand(100, 3)  # Generate random 3D data
hds = HDS()
hds.display_hologram(data)
