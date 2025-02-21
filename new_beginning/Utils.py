import numpy as np

def calculate_snr(noise_points, signal_points, N_bins):
    if len(noise_points) == 0:
        return 0.0, 0.0

    hist_noise, _ = np.histogram(noise_points, bins=N_bins, range=(0, 1))
    hist_signal, _ = np.histogram(signal_points, bins=N_bins, range=(0, 1))

    A_s = np.max(hist_signal)
    A_n = np.mean(hist_noise)

    SNR = A_s / A_n
    SNR_db = 10 * np.log10(SNR)

    return SNR, SNR_db


def generate_one_dimensional_points(N_n, N_s, x0, sigma, N_bins):
    noise_points = np.random.uniform(0, 1, N_n)
    signal_points = np.random.normal(x0, sigma, N_s)
    points = np.concatenate([noise_points, signal_points])

    # Вычисление реального SNR
    SNR, SNR_db = calculate_snr(noise_points, signal_points, N_bins)
    return points, SNR, SNR_db