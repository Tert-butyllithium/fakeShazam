import os
import shutil
import read_music
import pickle

DEBUG_MODE = False
META_DIR = 'data/metadata/'
MUSIC_DIR = 'data/music/'


def init():
    f = os.listdir(MUSIC_DIR)
    cnt = 1
    inverted_index = {}
    name_dict = {}
    for file in f:
        fingerprint = read_music.get_fingerprint(MUSIC_DIR + file)
        for landmark in fingerprint:
            if landmark[0] not in inverted_index:
                inverted_index[landmark[0]] = [(cnt, landmark[1])]
            else:
                inverted_index[landmark[0]].append((cnt, landmark[1]))

        name_dict[cnt] = file
        if DEBUG_MODE and cnt > 5:
            break
        cnt += 1
    inverted_index_saved = open(META_DIR + 'inverted_index.meta', 'wb')
    pickle.dump(inverted_index, inverted_index_saved)
    name_dict_saved = open(META_DIR + 'name_dict.meta', 'wb')
    pickle.dump(name_dict, name_dict_saved)


if __name__ == '__main__':
    if DEBUG_MODE:
        shutil.rmtree(META_DIR)
    if not os.path.exists(META_DIR):
        os.mkdir(META_DIR)
        init()
    print('Done!')
