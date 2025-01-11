import numpy as np
import matplotlib.pyplot as plt
import colorsys

hue_min = 0.5
hue_max = 0.9
saturation = 0.7
lightness = 0.8
hue_range = hue_max - hue_min

def make_gradient(s_x, s_y, grid_size, plot_num):
    # Discretize plot
    square_size = 1.0 / grid_size

    # Calculating point in each squares
    counts = np.zeros((grid_size, grid_size))
    for i in range(len(s_x)):
        counts[int(np.floor(s_x[i] / square_size))][int(np.floor(s_y[i] / square_size))] += 1
    max_count = np.max(counts)

    # Generate gradient and image
    gradient = np.zeros((grid_size, grid_size, 3))

    for i in range(grid_size):
        for j in range(grid_size):
            count = counts[i, j]
            hue_shift = count / max_count
            hue = hue_min + hue_range * hue_shift

            # HSL to RGB
            r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
            gradient[i, j] = [r, g, b]

    # Shows
    plt.subplot(2, 2, plot_num)
    plt.imshow(gradient, extent=[0, 1, 0, 1])
    plt.title('Grid_size = ' + str(grid_size))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)

def GRADIENT_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y):
    # Shows
    fig = plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    plt.scatter(s_p_x, s_p_y, color='red')
    plt.scatter(s_n_x, s_n_y, color='black')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.title('Signal')

    make_gradient(s_x, s_y, 5, 2)
    make_gradient(s_x, s_y, 15, 3)
    make_gradient(s_x, s_y, 25, 4)

    plt.tight_layout()
    fig.suptitle('GRADIENT method (MY)')
    plt.show()