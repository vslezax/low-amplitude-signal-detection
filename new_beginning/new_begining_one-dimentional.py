from new_beginning.HISTOGRAM_method import histogram_method
from Utils import generate_one_dimensional_points

N_n = 1000
N_s = 0
x0_true = 0.7
sigma = 0.1
N_bins = 100

points, SNR_real, SNR_db_real = generate_one_dimensional_points(N_n, N_s, x0_true, sigma, N_bins)

# Метод гистограммы
x0_estimated, SNR_alg, SNR_db_alg = histogram_method(points, N_bins, sigma=0.1)
print(f"Оценка x0: {x0_estimated}")
print(f"SNR (безразмерное): {SNR_alg:.2f}")
print(f"SNR (дБ): {SNR_db_alg:.2f}")
print(f"Реальный SNR (безразмерное): {SNR_real:.2f}")
print(f"Реальный SNR (дБ): {SNR_db_real:.2f}")