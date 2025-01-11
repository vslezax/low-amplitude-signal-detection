import numpy as np
import matplotlib.pyplot as plt
from Utils import histogram_otsu, histogram_median

from Utils import show_reference_signal_left

# RANSAC parameters
n_iter = 1000  # Iteration count
best_model = None
max_inliers = 0

def RANSAC_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y):
    # Combine x and y coord
    points = np.column_stack((s_x, s_y))

    # RANSAC
    for _ in range(n_iter):
        # Random 3 points
        sample_idx = np.random.choice(len(points), 3, replace=False)
        sample_points = points[sample_idx]

        # hypothetical center
        center = np.mean(sample_points, axis=0)

        # Distances calculation
        distances = np.linalg.norm(points - center, axis=1)

        # Choosing inliners
        threshold = histogram_median(distances)
        inliers = distances <= threshold
        num_inliers = np.sum(inliers)

        max_inliers = 0
        # Updating
        if num_inliers > max_inliers:
            max_inliers = num_inliers
            best_model = {'center': center, 'inliers': inliers}

    # Results
    final_center = best_model['center']
    inliers = best_model['inliers']

    # Shows
    fig = plt.figure(figsize=(10, 6))
    show_reference_signal_left(s_p_x, s_p_y, s_n_x, s_n_y)

    plt.subplot(1, 2, 2)
    plt.scatter(points[~inliers, 0], points[~inliers, 1], color='black')
    plt.scatter(points[inliers, 0], points[inliers, 1], color='red')
    plt.scatter(*final_center, color='blue', s=100, label='Estimated Center', marker='x')
    plt.title('RANSAC-based Signal Separation')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.show()