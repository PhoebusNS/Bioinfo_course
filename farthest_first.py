__author__ = 'Jacques'

import os
from math import sqrt


def point_dist(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i]-b[i])**2
    return sqrt(d)


def dist_set(a, s):
    l = [point_dist(a, b) for b in s]
    return min(l)


def interpreter(conn):
    first = conn.readline().strip().split(' ')
    kk = int(first[0])
    mm = int(first[1])
    point_sett = list()
    for raw_line in conn:
        point = raw_line.strip().split(' ')
        float_point = [float(i) for i in point]
        point_sett.append(float_point)
    return kk, mm, point_sett


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    with open('dataset_10926_14.txt', 'r') as f:
        k, m, point_set = interpreter(f)
    centers = list()
    centers.append(point_set.pop(0))
    while len(centers) < k:
        maxi = 0
        for i, point in enumerate(point_set):
            d = dist_set(point, centers)
            if d > maxi:
                maxi = d
                index = i
        centers.append(point_set.pop(index))
    with open('farthest.txt', 'w') as g:
        for point in centers:
            g.write(' '.join(map(str, point))+'\n')