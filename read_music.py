import operator
from hashlib import sha256
from pydub import AudioSegment
import numpy as np
import itertools

# import from project
import fingerprint


def gen_sha256(filepath):
    blocksize = 1 << 16
    sha = sha256()
    with open(filepath, 'rb') as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            sha.update(buf)
    return sha.hexdigest()


def get_framerate_and_channels(filepath):
    music_file = AudioSegment.from_file(filepath)
    data = np.frombuffer(music_file.raw_data, np.int16)
    channels = []

    for channel in range(music_file.channels):
        channels.append(data[channel::music_file.channels])
    # print(music_file.frame_rate)
    return music_file.frame_rate, channels


def get_fingerprint(filepath):
    res = set()
    frame_rate, channels = get_framerate_and_channels(filepath)
    for channel in channels:
        spectrum = fingerprint.get_spectrum(channel, frame_rate)
        peaks = fingerprint.get_constellation_map(spectrum)
        fp = fingerprint.generate_hashes(peaks)
        res = res.union(fp)

    return res


def get_peaks(filepath):
    res = []
    frame_rate, channels = get_framerate_and_channels(filepath)
    for channel in channels[:1]:
        spectrum = fingerprint.get_spectrum(channel, frame_rate)
        peaks = fingerprint.get_constellation_map(spectrum)
        # print(peaks.__len__(), peaks)
        res += peaks
    # return list(itertools.chain.from_iterable(zip(res[0], res[1])))
    # res.sort(key=operator.itemgetter(1))
    return res


# test
if __name__ == '__main__':
    ans = get_peaks('data/music/1848.mp3')
    print(ans)
    print(get_peaks('sub1848.mp3'))
