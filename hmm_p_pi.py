__author__ = 'Jacques'

from os import chdir


def interpreter(conn):
    path = conn.readline().strip()
    conn.readline()
    states = conn.readline().strip().split(' ')
    conn.readline()
    transit = dict()
    while True:
        l = conn.readline()
        if l == '' or l[0:2] == '--':
            break
        ll = l.strip().split('\t')
        if len(ll) == len(states)+1:
            dd = dict()
            for i, s in enumerate(states):
                dd[s] = float(ll[i+1])
            transit[ll[0]] = dd
    return path, states, transit

if __name__ == '__main__':
    chdir('C:\\Users\\Jacques\\Downloads')
    with open('dataset_11594_2.txt', 'r') as f:
        path, states, transit = interpreter(f)
    p = 1
    for index in range(len(path)):
        if index == 0:
            p /= len(states)
        else:
            p *= transit[path[index-1]][path[index]]
    print(p)
