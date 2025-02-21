import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def histogram_method(points, N_bins=100, sigma=0.1):
    # Построение гистограммы
    bins = np.linspace(0, 1, N_bins + 1)
    hist, _ = np.histogram(points, bins=bins)

    # Предполагаем, что шум равномерно распределен и вычитаем его модель
    uniform_hist = np.full(N_bins, len(points) / N_bins)
    diff_hist = hist - uniform_hist

    # Амплитуда сигнала (A_s) — наибольшее значение разности
    # Амплитуда шума (A_n) — среднее значение разности
    A_s = np.max(hist)
    A_n = np.mean(hist)
    SNR = A_s / A_n
    SNR_db = 10 * np.log10(SNR)

    # Гистограмма всех точек
    plt.figure(figsize=(12, 10))
    plt.subplot(4, 1, 1)
    plt.hist(points, bins=bins, color='blue', alpha=0.7, label='Все точки')
    plt.title('Гистограмма всех точек')
    plt.xlabel('x')
    plt.ylabel('Количество точек')
    plt.legend()

    # Гистограмма разности (сигнал)
    plt.subplot(4, 1, 2)
    plt.bar(bins[:-1], diff_hist, width=1 / N_bins, color='green', alpha=0.7, label='Разность (сигнал)')
    plt.title('Гистограмма разности (сигнал)')
    plt.xlabel('x')
    plt.ylabel('Разность')
    plt.legend()

    # Функция для минимизации
    def objective(x0):
        # Моделируем нормальное распределение вокруг x0
        model = np.exp(-0.5 * ((bins[:-1] - x0) / sigma) ** 2)
        model /= model.sum()
        model *= len(points)

        # Сравниваем с разностью гистограмм
        return np.sum((diff_hist - model) ** 2)

    # Начальное предположение для x0 (пик разности гистограмм)
    x0_guess = bins[np.argmax(diff_hist)]

    # Минимизация ошибки
    result = minimize(objective, x0_guess, bounds=[(0, 1)])
    x0_estimated = result.x[0]

    # Визуализация результата
    plt.subplot(4, 1, 3)
    plt.bar(bins[:-1], diff_hist, width=1 / N_bins, color='green', alpha=0.7, label='Разность (сигнал)')
    plt.axvline(x=x0_estimated, color='red', linestyle='--', label=f'Оценка x0: {x0_estimated:.3f}')
    plt.title('Результат оценки x0')
    plt.xlabel('x')
    plt.ylabel('Разность')
    plt.legend()

    # Вывод SNR
    plt.subplot(4, 1, 4)
    plt.text(0.1, 0.5, f'SNR (безразмерное): {SNR:.2f}\nSNR (дБ): {SNR_db:.2f}\nN_bins: {N_bins:.1f}', fontsize=12,
             bbox=dict(facecolor='yellow', alpha=0.5))
    plt.axis('off')  # Отключаем оси для текстового вывода
    plt.title('SNR')

    plt.tight_layout()
    plt.show()

    return x0_estimated, SNR, SNR_db