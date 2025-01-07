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

def threshold_distance_method(s_x, s_y):
    distances = []
    # Calculating distances
    for i in range(len(s_x)):
        distances.append(calculate_distance(i, s_x, s_y))

    # Showing distances distribution
    plt.figure()
    plt.hist(distances, bins=50)
    plt.show()