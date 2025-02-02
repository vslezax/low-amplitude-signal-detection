from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import matplotlib.pyplot as plt
from Utils import show_reference_signal_left

def LOF_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y, neighbors=20, contamination=0.1):
    s_x = np.array(s_x)
    s_y = np.array(s_y)
    points = np.column_stack((s_x, s_y))

    lof = LocalOutlierFactor(n_neighbors=neighbors)
    lof_scores = -lof.fit_predict(points)

    # Находим границу по 10% самых больших значений LOF
    threshold = np.percentile(lof_scores, 100 * (1 - contamination))
    signal_mask = lof_scores < threshold  # Если LOF ниже порога, это сигнал

    # Визуализация
    fig = plt.figure(figsize=(10, 6))
    show_reference_signal_left(s_p_x, s_p_y, s_n_x, s_n_y)

    plt.subplot(1, 2, 2)
    plt.scatter(s_x[signal_mask], s_y[signal_mask], color='red', label='Signal')
    plt.scatter(s_x[~signal_mask], s_y[~signal_mask], color='black', label='Noise')
    plt.title('LOF')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.show()
