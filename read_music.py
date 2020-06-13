from hashlib import sha256
from pydub import AudioSegment
import numpy as np

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
    data = np.fromstring(music_file.raw_data, np.int16)
    channels = []

    for channel in range(music_file.channels):
        channels.append(data[channel::music_file.channels])
    print(music_file.frame_rate)
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


if __name__ == '__main__':
    print(get_fingerprint('C:\\Users\\lanranli\\PycharmProjects\\fakeShazam\\data\\music\\1848.mp3'))
