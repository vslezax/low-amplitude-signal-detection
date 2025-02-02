from sklearn.mixture import GaussianMixture
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_reference_signal_left

# DMM - Gaussian Mixture Model
# Гауссово смесевое моделирование
def GMM_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y, n_components=3):
    '''
    s_x = np.array(s_x)
    s_y = np.array(s_y)
    points = np.column_stack((s_x, s_y))

    # Обучаем GMM (две компоненты: сигнал и шум)
    gmm = GaussianMixture(n_components=2, covariance_type='full', random_state=42)
    gmm.fit(points)
    labels = gmm.predict(points)

    # Определяем, какой кластер – сигнал (берём тот, у которого больше плотность)
    if gmm.weights_[0] > gmm.weights_[1]:
        signal_cluster = 0
    else:
        signal_cluster = 1
    '''
    s_x = np.array(s_x)
    s_y = np.array(s_y)
    points = np.column_stack((s_x, s_y))

    gmm = GaussianMixture(n_components=n_components, covariance_type='diag', random_state=42)
    gmm.fit(points)
    labels = gmm.predict(points)

    # Ищем кластер с наибольшей плотностью
    cluster_densities = gmm.weights_ / np.prod(gmm.covariances_, axis=1)
    signal_cluster = np.argmax(cluster_densities)

    # Shows
    fig = plt.figure(figsize=(10, 6))
    show_reference_signal_left(s_p_x, s_p_y, s_n_x, s_n_y)

    plt.subplot(1, 2, 2)
    plt.scatter(s_x[labels == signal_cluster], s_y[labels == signal_cluster], color='red', label='Signal')
    plt.scatter(s_x[labels != signal_cluster], s_y[labels != signal_cluster], color='black', label='Noise')
    plt.title('GMM')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.show()

