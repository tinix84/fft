import numpy as np
from numpy.fft import rfft, irfft
from pathlib import Path

import yaml

"""App configuration."""
cfg_file_path_obj = (Path(__file__).parent / Path('./config.yaml'))
full_CONFIG_YAML_FILE = str(cfg_file_path_obj.absolute())
with open(full_CONFIG_YAML_FILE, 'r') as ymlfile:
    cfg = yaml.full_load(ymlfile)
MATLAB_FOLDER = str(cfg['fft']['MATLAB_FOLDER'])

try:
    import matlab.engine
    import matlab
    matlab_not_available = False
except ImportError:
    matlab_not_available = True


def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


def get_matlab_calc_time_series(frequency, coefficients):
    eng = matlab.engine.start_matlab()
    eng.addpath(MATLAB_FOLDER, nargout=0)
    mat_frequency = matlab.double(frequency.tolist())
    mat_coefficients = matlab.double(coefficients.tolist())
    [t, s] = eng.calc_time_series(mat_frequency, mat_coefficients)
    return [t, s]


def get_matlab_calc_fourier_coefficients(time, signal):
    eng = matlab.engine.start_matlab()
    eng.addpath(MATLAB_FOLDER, nargout=0)
    mat_time = matlab.double(time.tolist())
    mat_signal = matlab.double(signal.tolist())
    # https://ch.mathworks.com/help/matlab/apiref/matlab.engine.matlabengine-class.html
    [f_matlab, c_matlab] = eng.calc_fourier_coefficients(mat_time, mat_signal,
                            nargout=2)
    f = np.asarray(f_matlab)[0]
    c = np.asarray(c_matlab)[0]
    return [f, c]


def get_octave_calc_time_series(frequency, coefficients):
    eng = matlab.engine.start_matlab()
    eng.addpath(MATLAB_FOLDER, nargout=0)
    mat_frequency = matlab.double(frequency.tolist())
    mat_coefficients = matlab.double(coefficients.tolist())
    [t, s] = eng.calc_time_series(mat_frequency, mat_coefficients)
    return [t, s]


def get_octave_calc_fourier_coefficients(time, signal):
    eng = matlab.engine.start_matlab()
    eng.addpath(MATLAB_FOLDER, nargout=0)
    mat_time = matlab.double(time.tolist())
    mat_signal = matlab.double(signal.tolist())
    # https://ch.mathworks.com/help/matlab/apiref/matlab.engine.matlabengine-class.html
    [f_matlab, c_matlab] = eng.calc_fourier_coefficients(mat_time, mat_signal,
                            nargout=2)
    f = np.asarray(f_matlab)[0]
    c = np.asarray(c_matlab)[0]
    return [f, c]


def calc_time_series(frequency, coefficients, matlab_engine=None):
    """ Get the FFT of a given signal and corresponding frequency bins.

    Parameters:
        frequency  - frequency vector
        coefficients - fft coeffients
        matlab_engine - boolean to execute with matlab or numpy
    Returns:
        (freq, c_fft) - tuple of complex coefficient and realative frequencies
    """
    if matlab_engine is None or matlab_not_available:
        print("matlab_not_available")
        # build dft format
        _ = max(frequency)
        N = coefficients.size
        s = irfft(coefficients)*N
        t = np.linspace(0,  stop=1 / frequency[1], num=s.size)

        # len_fft = len(coefficients)
        # s = np.fft.ifft(coefficients)
        # t = np.linspace(0,  stop=1 / frequency[1], num=s.size)
        return [t, s]
    else:
        [t, s] = get_matlab_calc_time_series(frequency, coefficients)
        return [t, s]


def calc_fourier_coefficients(time, signal, matlab_engine=None):
    """ Get the FFT of a given signal and corresponding frequency bins.

    Parameters:
        signal  - signal amplitude
        time - time vector of signal
        matlab_engine - boolean to execute with matlab or numpy
    Returns:
        (freq, c_fft) - tuple of complex coefficient and realative frequencies
    """
    if matlab_engine is None:
        print("matlab_not_available")
        N = signal.size
        dt = float(time[1]-time[0])
        c_fft = rfft(signal, n=N, norm=None)*2/N
        freq = np.fft.rfftfreq(N, d=dt)
        return freq, c_fft
    else:
        [f, c] = get_matlab_calc_fourier_coefficients(time, signal)
        return [f, c]
