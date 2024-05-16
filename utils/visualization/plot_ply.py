import matplotlib.pyplot as plt
import numpy as np
from plyfile import PlyData
 
def visualize_point_cloud(ply_file_path):
    ply_data = PlyData.read(ply_file_path)
    vertex = ply_data['vertex']

    # Extracting coordinates
    x = np.array(vertex['x'])
    y = np.array(vertex['y'])
    z = np.array(vertex['z'])

    # Plotting the point cloud
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=1, c=z, cmap='viridis', marker='.')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()