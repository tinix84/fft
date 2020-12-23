from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

from .context import fft

try:
    import matlab.engine
    import matlab
    matlab_engine_is_available = True
except ImportError:
    matlab_engine_is_available = False


def test_numpy_fft_and_reverse():
    # fft test
    t = np.linspace(start=0, stop=1, num=1001, endpoint=True)
    s = 40*signal.square(2 * np.pi * 5 * t)

    fig = plt.figure()
    ax = fig.add_subplot(311)
    ax.plot(t, s)

    [f, c] = calc_fourier_coefficients(t, s)
    ax = fig.add_subplot(312)
    ax.semilogx(f, 20*np.log10(np.abs(c)))

    [tinv, sinv] = calc_time_series(f, c)
    ax = fig.add_subplot(313)
    ax.plot(tinv, sinv)
    plt.show()


def test_compare_fft_and_fourier_formula():
    # fft test
    fsw = 300
    Apk = 40
    t = np.linspace(start=0, stop=1, num=100*fsw, endpoint=True)
    s = Apk*signal.square(2 * np.pi * fsw * t)

    fig = plt.figure()
    ax = fig.add_subplot(311)
    ax.plot(t, s)

    [f, c] = calc_fourier_coefficients(t, s)
    [fs, cs] = calc_square_wave_DFT(ampl_pkpk=2*Apk,fsw=fsw, n_harmonics=30)
    ax = fig.add_subplot(312)
    ax.loglog(f, np.abs(c), fs, np.abs(cs))

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

    assert rmse(f, f_matlab) < 1e-6, "freq vector matches"
    assert rmse(abs(c_matlab), abs(c)) < 1e-6, "c vector matches"
    print("freq_vector_diff {}".format(rmse(f,f_matlab)))
    print("amp_vector_diff {}".format(rmse(abs(c_matlab), abs(c))))


def test_calc_time_series_numpy_vs_matlab():
    raise(NotImplementedError)


def test_get_N_highest_peaks(n_peaks=10):
    t = np.linspace(start=0, stop=1, num=1001, endpoint=True)
    s = signal.square(10 * np.pi * 5 * t)
    [f, c] = calc_fourier_coefficients(t, s)
    freq_pk, c_pk = get_N_highest_peaks(frequency = f, coefficients = c, number_of_peaks = n_peaks)

    for fp, hp in zip(freq_pk, c_pk):
        print(f'Freq: {fp:.2e} Hz Abs:{abs(hp):.2e}')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.semilogx(freq_pk, (abs(c_pk)), label='numpy')
    plt.show()


if __name__ == "__main__":
    test_numpy_fft_and_reverse()
    test_compare_fft_and_fourier_formula()
    if matlab_engine_is_available:
        test_calc_fourier_coefficients_numpy_vs_matlab()
        test_calc_time_series_numpy_vs_matlab()
    test_get_N_highest_peaks()

