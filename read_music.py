from hashlib import sha256
from pydub import AudioSegment
import numpy as np


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


if __name__ == '__main__':
    pass
