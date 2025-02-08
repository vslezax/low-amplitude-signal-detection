import numpy as np
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

def SNR_to_points_count_iterations(SNR, total_points_count):
    N_noise = total_points_count // (1 + SNR)
    N_signal = SNR * np.sqrt(N_noise)

    while abs(N_signal + N_noise - total_points_count) > 1:
        N_noise = total_points_count - N_signal
        N_signal = SNR * np.sqrt(N_noise)

    N_signal = int(N_signal)
    N_noise = int(N_noise)

    return N_signal, N_noise

def SNR_to_points_count_quadratic(SNR, total_points_count):
    N_signal = (np.sqrt(SNR ** 4 + 4 * SNR ** 2 * total_points_count) - SNR ** 2) / 2
    N_signal = int(N_signal)
    N_noise = total_points_count - N_signal

    return N_signal, N_noise

def show_reference_signal_left(s_p_x, s_p_y, s_n_x, s_n_y):
    plt.subplot(1, 2, 1)
    plt.scatter(s_p_x, s_p_y, color='red')
    plt.scatter(s_n_x, s_n_y, color='black')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.title('Signal')

# Otsu method
def histogram_otsu(histogram):
    return threshold_otsu(histogram)

def histogram_median(histogram):
    return np.median(histogram)