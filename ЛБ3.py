import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate
from scipy.fft import fft, fftfreq, fftshift

# Параметри сигналу s1 (пилкоподібний)
A1 = 4  # амплітуда, В
tau1 = 2e-3  # час наростання
tau2 = 2e-3  # час спадання
T1 = tau1 + tau2 + 1e-3  # загальна тривалість імпульсу

# Параметри сигналу s2 (двосторонній експоненційний)
A2 = 4  # амплітуда, В
tau_exp = 3e-3  # часова константа

# Дискретизація
Fs = 100000  # частота дискретизації
t = np.linspace(-0.01, 0.01, int(0.02 * Fs))

# Сигнал s1(t) — пилкоподібний імпульс
s1 = np.zeros_like(t)
t0 = 0  # центр
s1[(t >= t0 - tau1) & (t < t0)] = A1 * (t[(t >= t0 - tau1) & (t < t0)] - (t0 - tau1)) / tau1
s1[(t >= t0) & (t <= t0 + tau2)] = A1 * (1 - (t[(t >= t0) & (t <= t0 + tau2)] - t0) / tau2)

# Сигнал s2(t) — двосторонній експоненційний імпульс
s2 = np.where(t < 0, A2 * np.exp(t / tau_exp), A2 * np.exp(-t / tau_exp))

# Автокореляційна функція s1
corr_s1 = correlate(s1, s1, mode='full')
lags = np.linspace(-t[-1], t[-1], len(corr_s1))

# Взаємна кореляційна функція s1 та s2
corr_s1s2 = correlate(s1, s2, mode='full')

# Спектр сигналу s1
s1_fft = fftshift(fft(s1))
freqs = fftshift(fftfreq(len(s1), d=1/Fs))
energy_spectrum = np.abs(s1_fft)**2

# Перетворення Фур’є автокореляційної функції s1
corr_fft = fftshift(fft(corr_s1))
corr_freqs = fftshift(fftfreq(len(corr_s1), d=1/Fs))

# Зберігаємо графіки
plt.figure(figsize=(10, 4))
plt.plot(t * 1000, s1)
plt.title("Рисунок 1 – Сигнал s₁(t) – Пилкоподібний імпульс")
plt.xlabel("Час, мс")
plt.ylabel("Амплітуда, В")
plt.grid()
plt.tight_layout()
plt.savefig("/mnt/data/fig1_s1_signal.png")
plt.close()

plt.figure(figsize=(10, 4))
plt.plot(t * 1000, s2)
plt.title("Рисунок 2 – Сигнал s₂(t) – Двосторонній експоненційний імпульс")
plt.xlabel("Час, мс")
plt.ylabel("Амплітуда, В")
plt.grid()
plt.tight_layout()
plt.savefig("/mnt/data/fig2_s2_signal.png")
plt.close()

plt.figure(figsize=(10, 4))
plt.plot(lags * 1000, corr_s1)
plt.title("Рисунок 3 – Автокореляційна функція сигналу s₁(t)")
plt.xlabel("Зсув, мс")
plt.ylabel("Rₛ₁(τ)")
plt.grid()
plt.tight_layout()
plt.savefig("/mnt/data/fig3_autocorr_s1.png")
plt.close()

plt.figure(figsize=(10, 4))
plt.plot(lags * 1000, corr_s1s2)
plt.title("Рисунок 5 – Взаємна кореляційна функція сигналів s₁(t) та s₂(t)")
plt.xlabel("Зсув, мс")
plt.ylabel("Rₛ₁ₛ₂(τ)")
plt.grid()
plt.tight_layout()
plt.savefig("/mnt/data/fig5_crosscorr_s1s2.png")
plt.close()

plt.figure(figsize=(10, 4))
plt.plot(freqs / 1000, energy_spectrum)
plt.title("Рисунок 7 – Енергетичний спектр сигналу s₁(t)")
plt.xlabel("Частота, кГц")
plt.ylabel("|S(f)|²")
plt.grid()
plt.tight_layout()
plt.savefig("/mnt/data/fig7_energy_spectrum_s1.png")
plt.close()

plt.figure(figsize=(10, 4))
plt.plot(corr_freqs / 1000, np.abs(corr_fft))
plt.title("Рисунок 8 – Перетворення Фур’є автокореляційної функції Rₛ₁(τ)")
plt.xlabel("Частота, кГц")
plt.ylabel("Модуль спектру")
plt.grid()
plt.tight_layout()
plt.savefig("/mnt/data/fig8_fft_autocorr_s1.png")
plt.close()

"/mnt/data/ — графіки збережені повторно після відновлення сесії."
