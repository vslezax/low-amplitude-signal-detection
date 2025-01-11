import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
import matplotlib.pyplot as plt

from Utils import show_reference_signal_left

def MST_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y):
    # Combine x and y coord
    points = np.column_stack((s_x, s_y))

    # Distance matrix
    dist_matrix = distance_matrix(points, points)

    # MST
    mst = minimum_spanning_tree(dist_matrix).toarray()

    # Export edge lenght greater than 0
    edge_lengths = mst[mst > 0]

    # Threshold = median
    threshold = np.median(edge_lengths)

    # Filtering mst
    # (mst <= threshold) is a logic matrix, where 'True' - edges with length less than threshold
    filtered_mst = (mst <= threshold) * mst

    # Finding clusters
    # n_clusters - found clusters count
    n_clusters, labels = connected_components(csgraph=filtered_mst, directed=False)

    # Showing
    fig = plt.figure(figsize=(10, 6))
    show_reference_signal_left(s_p_x, s_p_y, s_n_x, s_n_y)

    plt.subplot(1, 2, 2)
    for cluster_id in range(n_clusters):
        cluster_points = points[labels == cluster_id]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {cluster_id}')
    plt.legend()
    plt.title('Clusters after MST Filtering')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    fig.suptitle('MST method')
    plt.show()

