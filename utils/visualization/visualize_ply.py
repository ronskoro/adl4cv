import open3d as o3d

def visualize_ply(filepath):
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(filepath)

    # Visualize the point cloud
    o3d.visualization.draw_geometries([pcd])

# Specify the path to your PLY file
file_path_1 = "../../data/scans/scene0000_00/scene0000_00_vh_clean_2.ply" # Point cloud
file_path_2 = "../../data/scans/scene0000_00/scene0000_00_vh_clean_2.labels.ply" # Labels
file_path_3 = "../../data/scans/scene0000_00/scene0000_00_vh_clean.ply" # Full Scan
visualize_ply(file_path_2)