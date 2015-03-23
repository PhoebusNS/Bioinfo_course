__author__ = 'Jacques'

import os


def trie_matcher(genome, root, conn):
    n = len(genome)
    for i in range(n):
        current = root
        letter = genome[i]
        step = 0
        while letter in current:
            current = current[letter]
            if '_l' in current:
                conn.write(str(i)+' ')
                break
            step += 1
            if i+step >= n:
                break
            else:
                letter = genome[i + step]


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    f = open('dataset_294_8.txt', 'r')
    genome = f.readline()
    root = dict()
    for line in f:
        current = root
        word = line.strip()
        for letter in word:
            current = current.setdefault(letter, dict())
        current['_l'] = '_l'
    f.close()

    os.chdir('C:\\Users\\Jacques\\Downloads\\Outputs')
    with open('triematch_out.txt', 'w') as g:
        trie_matcher(genome, root, g)