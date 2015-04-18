__author__ = 'Jacques'

import os


def interpreter(conn):
    nn = int(conn.readline().strip())
    jj = int(conn.readline().strip())
    dd = list()
    for lin in conn:
        dd.append(list(map(int, lin.strip().split(' '))))
    return nn, jj, dd


def limb_length(index):
    curr_min = float('inf')
    for i in range(n):
        if i == index:
            continue
        else:
            for ii in range(i, n):
                if ii == index:
                    continue
                else:
                    curr = d[i][index]+d[index][ii]-d[i][ii]
                    curr /= 2
                    if curr < curr_min:
                        curr_min = curr
    return int(curr_min)


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    with open('dataset_10329_11.txt', 'r') as f:
        n, j, d = interpreter(f)
    print(d)
    limb = limb_length(j)
    print(limb)