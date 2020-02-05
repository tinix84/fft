from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

import sys, os
from sklearn.metrics import mean_squared_error

# Make sure that the application source directory (this directory's parent) is
# on sys.path.

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

from fft import calc_fourier_coefficients, calc_time_series

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def test_numpy_fft_and_reverse():
    # fft test
    t = np.linspace(start=0, stop=1, num=1001, endpoint=True)
    s = signal.square(2 * np.pi * 5 * t)

    fig = plt.figure()
    ax = fig.add_subplot(311)
    ax.plot(t, s)

    [f, c] = calc_fourier_coefficients(t, s)
    ax = fig.add_subplot(312)
    ax.semilogx(f, 20*np.log10(abs(c)))

    [tinv, sinv] = calc_time_series(f, c)
    ax = fig.add_subplot(313)
    ax.plot(tinv, sinv)
    plt.show()

def test_calc_fourier_coefficients_numpy_vs_matlab():
    # fft test
    t = np.linspace(start=0, stop=1, num=1001, endpoint=True)
    s = signal.square(10 * np.pi * 5 * t)
    [f, c] = calc_fourier_coefficients(t, s)
    [f_matlab, c_matlab] = calc_fourier_coefficients(time=t, signal=s, matlab_engine=True)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.semilogx(f_matlab, (abs(c_matlab)), label='matlab')
    ax.semilogx(f, (abs(c)), label='numpy')
    plt.show()

    assert mean_squared_error(f, f_matlab) < 1e-6, "freq vector matches"
    assert mean_squared_error(abs(c_matlab), abs(c)) < 1e-6, "c vector matches"

def test_calc_time_series_numpy_vs_matlab():
    raise(NotImplementedError)

if __name__ == "__main__":
    test_numpy_fft_and_reverse()
    test_calc_fourier_coefficients_numpy_vs_matlab()
    test_calc_time_series_numpy_vs_matlab()

