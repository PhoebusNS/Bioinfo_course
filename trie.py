__author__ = 'Jacques'

import os


def printer(start, node):
    for key, value in node.items():
        global n
        if key == '_l':
            continue
        else:
            n += 1
            g.write(str(start)+'->'+str(n)+':'+key+'\n')
            printer(n, value)

if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    f = open('dataset_294_4.txt', 'r')
    root = dict()
    for line in f:
        current = root
        word = line.strip()
        for letter in word:
            current = current.setdefault(letter, dict())
        current['_l'] = '_l'
    f.close()

    os.chdir('C:\\Users\\Jacques\\Downloads\\Outputs')
    g = open('trie_out.txt', 'w')
    n = 0
    printer(0, root)
    g.close()