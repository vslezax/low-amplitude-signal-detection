from MST_method import MST_method
from signal_generator import generate_signal_by_counts, show_signal, show_combined_signal
from THRESHOLD_DISTANCE_method import threshold_distance_method
from RANSAC_method import RANSAC_method


def main():
    s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y = generate_signal_by_counts(10, 20, .01, 0.5)
    # show_signal(s_p_x, s_p_y, n_p_x, n_p_y)
    # show_combined_signal(s_x, s_y)

    # threshold_distance_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    # MST_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    RANSAC_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)

main()