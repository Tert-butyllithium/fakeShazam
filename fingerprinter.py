from matplotlib import mlab, pyplot
from scipy import ndimage
import numpy as np

WIDOW_SIZE = 4096
OVERLAP_RATIO = 0.5
MIN_PEAK_AMP = 10
PEAK_NEAR_SIZE = 20
TIME_CONSTRAINT = (9, 200)


def get_spectrum(sample, freq, n_fft=WIDOW_SIZE, window=mlab.window_hanning,
                 n_overlap=int(WIDOW_SIZE * OVERLAP_RATIO)):
    """
    :param sample: per channel
    :param freq: music freq
    :param n_fft: number of data points per block of FFT
    :param window:
    :param n_overlap: number of overlaped
    :return: spectrum in log
    """

    spectrum, freqs, t = mlab.specgram(sample,
                                       NFFT=n_fft, Fs=freq, window=window, noverlap=n_overlap)
    spectrum[spectrum == 0] = 1
    spectrum = np.log(spectrum)

    print(np.max(spectrum))
    return spectrum


def get_constellation_map(spectrum, plot=False):
    local_max = ndimage.maximum_filter(spectrum, footprint=get_constellation_map.neighbor) == spectrum

    backgroud = spectrum == 0


get_constellation_map.struct = ndimage.generate_binary_structure(2, 1)
get_constellation_map.neighbor = ndimage.iterate_structure(get_constellation_map.struct, PEAK_NEAR_SIZE)

if __name__ == '__main__':
    pass
