import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import fft # noqa # pylint: disable=unused-import, wrong-import-position

from fft.fft import calc_fourier_coefficients, calc_time_series
from fft.fft_helpers import get_N_highest_peaks
from fft.fft_dft import calc_square_wave_DFT