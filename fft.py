import numpy as np
from numpy.fft import rfft, irfft
import scipy.fftpack

import matlab.engine
import matlab
 
FFT_MATLAB_FUNC_DIR = r"d:\OneDrive - NTB\105\06_Simulationen\functions\fft\matlab_func"

def calc_time_series(frequency, coefficients, matlab_engine = None):
    """ Get the FFT of a given signal and corresponding frequency bins.

    Parameters:
        frequency  - frequency vector
        coefficients - fft coeffients
        matlab_engine - boolean to execute with matlab or numpy
    Returns:
        (freq, c_fft) - tuple of complex coefficient and realative frequencies
    """
    if matlab_engine is None:
        # build dft format
        fs = max(frequency)
        s = irfft(coefficients)*fs
        t = np.linspace(0,  stop=1 / frequency[1], num=s.size)

        # len_fft = len(coefficients)
        # s = np.fft.ifft(coefficients)
        # t = np.linspace(0,  stop=1 / frequency[1], num=s.size)


        return [t, s]
    else:
        eng = matlab.engine.start_matlab()
        eng.addpath(FFT_MATLAB_FUNC_DIR,nargout=0)
        mat_frequency = matlab.double(frequency.tolist())
        mat_coefficients = matlab.double(coefficients.tolist())
        [f,c] = eng.calc_time_series(mat_frequency,mat_coefficients)
        return [f,c]

def calc_fourier_coefficients(time:np.array, signal:np.array, matlab_engine = None):
    """ Get the FFT of a given signal and corresponding frequency bins.

    Parameters:
        signal  - signal amplitude
        time - time vector of signal
        matlab_engine - boolean to execute with matlab or numpy
    Returns:
        (freq, c_fft) - tuple of complex coefficient and realative frequencies
    """
    if matlab_engine is None:
        N = signal.size
        dt = float(time[1]-time[0])
        c_fft = rfft(signal, n=N, norm=None)*2*dt
        freq = np.fft.rfftfreq(N, d=dt)
        return freq, c_fft
    else:
        eng = matlab.engine.start_matlab()
        eng.addpath(FFT_MATLAB_FUNC_DIR,nargout=0)
        mat_time = matlab.double(time.tolist())
        mat_signal = matlab.double(signal.tolist())
        # https://ch.mathworks.com/help/matlab/apiref/matlab.engine.matlabengine-class.html
        [f_matlab,c_matlab] = eng.calc_fourier_coefficients(mat_time,mat_signal, nargout=2)
        f = np.asarray(f_matlab)[0]
        c =np.asarray(c_matlab)[0]
        return [f,c]
    # end

if __name__ == "__main__":\
    pass
