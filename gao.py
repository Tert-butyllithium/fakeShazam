import read_music,fingerprint

if __name__ == '__main__':
    filename = '许嵩 - 有何不可.mp3'
    frame_rate,channels = read_music.get_framerate_and_channels(filename)

    for channel in channels:
        arr = fingerprint.get_spectrum(channel, frame_rate)
        tmp = fingerprint.get_constellation_map(arr, plot=True)
