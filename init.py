import os
import shutil
import read_music
import pickle

DEBUG_MODE = True
META_DIR = 'data/metadata/'
MUSIC_DIR = 'data/music/'


def init():
    f = os.listdir(MUSIC_DIR)
    cnt = 1
    name_dict = {}
    for file in f:
        fingerprint = read_music.get_fingerprint(MUSIC_DIR + file)
        for landmark in fingerprint:
            if landmark[0] not in name_dict:
                name_dict[landmark[0]] = [(cnt, landmark[1])]
            else:
                name_dict[landmark[0]].append((cnt, landmark[1]))
        # pickle.dump(fingerprint, saved)
        if DEBUG_MODE and cnt > 5:
            break
        cnt += 1
    saved = open(META_DIR + 'inverted_index.meta', 'wb')
    pickle.dump(name_dict, saved)


if __name__ == '__main__':
    if DEBUG_MODE:
        shutil.rmtree(META_DIR)
    if not os.path.exists(META_DIR):
        os.mkdir(META_DIR)
        init()
    else:
        print('Done!')
