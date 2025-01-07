import matplotlib.pyplot as plt
import numpy as np

def generate_signal():
    ...

def generate_signal_by_counts(signal_count, noise_count, sigma, loc):
    signal_points_x = []
    signal_points_y = []
    noise_points_x = []
    noise_points_y = []

    for i in range(signal_count):
        signal_points_x.append(np.random.normal(loc, sigma))
        signal_points_y.append(np.random.normal(loc, sigma))
    for i in range(noise_count):
        noise_points_x.append(np.random.uniform())
        noise_points_y.append(np.random.uniform())

    s_x = signal_points_x + noise_points_x
    s_y = signal_points_y + noise_points_y

    return s_x, s_y, signal_points_x, signal_points_y, noise_points_x, noise_points_y

def show_signal(signal_points_x, signal_points_y, noise_points_x, noise_points_y):
    plt.figure()
    plt.grid(1)
    plt.scatter(signal_points_x, signal_points_y, color='red')
    plt.scatter(noise_points_x, noise_points_y, color='black')

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('square')
    plt.show()

def show_combined_signal(s_x, s_y):
    plt.figure()
    plt.grid(1)
    plt.scatter(s_x, s_y, color='black')

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('square')
    plt.show()