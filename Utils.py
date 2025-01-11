import numpy as np
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

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