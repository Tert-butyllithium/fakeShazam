import read_music
import sys, os, pickle

INVERTED_INDEX_FILE = 'data/metadata/inverted_index.meta'
NAME_DICT_FILE = 'data/metadata/name_dict.meta'

if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        print('usage: gao.py <filename>')
        sys.exit(2)
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    fingerprint = read_music.get_fingerprint(filename)
    evaluate = {}
    # should be paralleled
    inverted_index_file = open(INVERTED_INDEX_FILE, 'rb')
    inverted_index = pickle.load(inverted_index_file)
    dict_name_file = open(NAME_DICT_FILE, 'rb')
    dict_name = pickle.load(dict_name_file)

    for landmark in fingerprint:
        if landmark[0] not in inverted_index:
            continue
        match = inverted_index[landmark[0]]
        for item in match:
            offset_delta = landmark[1] - item[1]
            idx = (item[0], offset_delta)
            if idx in evaluate:
                evaluate[idx] += 1
            else:
                evaluate[idx] = 1

    # print(evaluate)
    ans = list(evaluate.keys())
    ans.sort(key=lambda x: evaluate[x], reverse=True)
    print('Best match: ' + dict_name[ans[0][0]])
