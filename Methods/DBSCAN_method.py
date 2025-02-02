from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_reference_signal_left

# DBSCAN - Density-Based Spatial Clustering of Applications with Noise
# Основанная на плотности пространственная кластеризация для приложений с шумами
def DBSCAN_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y, eps=0.05, min_samples=5):
    s_x = np.array(s_x)
    s_y = np.array(s_y)
    points = np.column_stack((s_x, s_y))

    # DBSCAN кластеризация
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(points)

    # Шум помечается -1
    signal_mask = labels != -1

    # Shows
    fig = plt.figure(figsize=(10, 6))
    show_reference_signal_left(s_p_x, s_p_y, s_n_x, s_n_y)

    plt.subplot(1, 2, 2)
    plt.scatter(s_x[signal_mask], s_y[signal_mask], color='red', label='Signal')
    plt.scatter(s_x[~signal_mask], s_y[~signal_mask], color='black', label='Noise')
    plt.title('DBSCAN')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.show()

