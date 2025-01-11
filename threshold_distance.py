import numpy as np
import matplotlib.pyplot as plt

def calculate_distance(i, s_x, s_y):
    x = s_x[i]
    y = s_y[i]

    min_distance = 10
    for j in range(len(s_x)):
        if i == j: continue
        tmp_distance = np.sqrt(np.pow((x - s_x[j]), 2) + np.pow((y - s_y[j]), 2))
        if tmp_distance < min_distance:
            min_distance = tmp_distance

    return min_distance

def threshold_distance_method(s_x, s_y, s_p_x, s_p_y, s_n_x, s_n_y):
    distances = []
    # Calculating distances
    for i in range(len(s_x)):
        distances.append(calculate_distance(i, s_x, s_y))

    # Calculating bins by ratio (if 20 -> 0.05)
    discretization_ratio = 50
    distances_bins = [0] * discretization_ratio
    bin_width = 1.0/discretization_ratio
    for i in distances:
        bin_num = np.floor(i / bin_width)
        distances_bins[int(bin_num)] += 1

    # Finding max of function distances_bins
    threshold = bin_width
    max_count = 0
    for i in range(len(distances_bins)):
        if distances_bins[i] > max_count:
            threshold = (i + 1) * bin_width
            max_count = distances_bins[i]

    # Taking some space to the right by adding values greater than (max_value / 2)
    if max_count != 0:
        for i in range(int(threshold / bin_width) - 1, len(distances_bins)):
            if float(distances_bins[i]) < float(max_count) / 2.0:
                break
            threshold += bin_width

    # Filtering
    filtered_s_x = []
    filtered_s_y = []
    for i in range(len(distances)):
        if distances[i] < threshold:
            filtered_s_x.append(s_x[i])
            filtered_s_y.append(s_y[i])


    plt.figure()
    plt.scatter(s_p_x, s_p_y, color='red')
    plt.scatter(s_n_x, s_n_y, color='black')
    plt.scatter(filtered_s_x, filtered_s_y, color='yellow', marker='s')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(1)
    plt.show()