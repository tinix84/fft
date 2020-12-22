import numpy as np


def calc_pulse_wave_DFT(ampl_pkpk, duty, fsw, n_harmonics=10):
    """
     https://hydrogenaud.io/index.php?topic=107461.0
    """
    an = []
    for n in range(n_harmonics+1):
        if n == 0:
            an.append(ampl_pkpk*duty)
        else:
            an.append(2*ampl_pkpk/n/np.pi*np.sin(n*np.pi*duty))

    fv = fsw*np.arange(n_harmonics+1)
    return fv, np.array(an)


def calc_square_wave_DFT(ampl_pkpk, fsw, n_harmonics=10):
    """[Discrete fourier series for square wave signal
    https://hydrogenaud.io/index.php?topic=107461.0]

    Args:
        ampl_pkpk ([type]): [description]
        fsw ([type]): [description]
        n_harmonics (int, optional): [description]. Defaults to 10.

    Returns:
        [type]: [description]
    """
    an = []
    for n in range(n_harmonics+1):
        if n == 0:
            an.append(0)
        else:
            an.append(2*ampl_pkpk/n/np.pi*np.sin(n*np.pi/2))

    fv = fsw*np.arange(n_harmonics+1)
    return fv, np.array(an)


def calc_triangle_wave_DFT(ampl_pkpk, fsw, n_harmonics=10):
    """[Discrete fourier series for triangle wave signal
    https://hydrogenaud.io/index.php?topic=107461.0]

    Args:
        ampl_pkpk ([type]): [description]
        fsw ([type]): [description]
        n_harmonics (int, optional): [description]. Defaults to 10.

    Returns:
        [type]: [description]
    """
    an = []
    for n in range(n_harmonics+1):
        if n == 0:
            an.append(0)
        else:
            an.append(4*ampl_pkpk/(n*np.pi)**2)

    fv = fsw*np.arange(n_harmonics+1)
    return fv, np.array(an)


def calc_rectified_wave_DFT(ampl_pkpk, fsw, n_harmonics=10):
    """[Discrete fourier series for rectified sine wave signal
    https://hydrogenaud.io/index.php?topic=107461.0]

    Args:
        ampl_pkpk ([type]): [description]
        fsw ([type]): [description]
        n_harmonics (int, optional): [description]. Defaults to 10.

    Returns:
        [type]: [description]
    """
    an = []
    for n in range(n_harmonics+1):
        if n == 0:
            an.append(2*ampl_pkpk/(np.pi))
        else:
            an.append(-4*ampl_pkpk/np.pi/(4*n**2-1))

    fv = fsw*np.arange(n_harmonics+1)
    return fv, np.array(an)
