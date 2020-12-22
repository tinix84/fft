import numpy as np


def get_N_highest_peaks(frequency, coefficients, number_of_peaks):
    pk_index = np.argsort(abs(coefficients))[::-1][:number_of_peaks]
    freq_pk, c_pk = (frequency[pk_index], coefficients[pk_index])
    return freq_pk, c_pk
