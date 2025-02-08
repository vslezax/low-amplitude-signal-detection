from Utils import SNR_to_points_count_iterations, SNR_to_points_count_quadratic
from signal_generator import generate_signal_by_counts, show_signal

from Methods.DBSCAN_method import DBSCAN_method
from Methods.GRADIENT_method import GRADIENT_method
from Methods.LOF_method import LOF_method
from Methods.MST_method import MST_method
from Methods.SIFT_method import SIFT_LIKE_method
from Methods.THRESHOLD_DISTANCE_method import threshold_distance_method
from Methods.RANSAC_method import RANSAC_method
from Methods.GMM_method import GMM_method


def main():
    S_count, N_count = SNR_to_points_count_quadratic(3, 30)
    s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y = generate_signal_by_counts(S_count, N_count, .01, 0.5)
    show_signal(s_p_x, s_p_y, n_p_x, n_p_y)
    # show_combined_signal(s_x, s_y)

    threshold_distance_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    MST_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    RANSAC_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    GRADIENT_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    DBSCAN_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    GMM_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    LOF_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)
    SIFT_LIKE_method(s_x, s_y, s_p_x, s_p_y, n_p_x, n_p_y)

main()