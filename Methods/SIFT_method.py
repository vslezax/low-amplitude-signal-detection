from scipy.spatial import KDTree
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_reference_signal_left

def SIFT_LIKE_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y, r=0.1, density_threshold=5):
    s_x = np.array(s_x)
    s_y = np.array(s_y)
    points = np.column_stack((s_x, s_y))

    # KD-дерево для быстрого поиска соседей
    tree = KDTree(points)
    densities = np.array([len(tree.query_ball_point(p, r)) for p in points])

    # Фильтр по плотности
    signal_mask = densities > density_threshold

    # Визуализация
    fig = plt.figure(figsize=(10, 6))
    show_reference_signal_left(s_p_x, s_p_y, s_n_x, s_n_y)

    plt.subplot(1, 2, 2)
    plt.scatter(s_x[signal_mask], s_y[signal_mask], color='red', label='Signal')
    plt.scatter(s_x[~signal_mask], s_y[~signal_mask], color='black', label='Noise')
    plt.title('SIFT')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.show()
