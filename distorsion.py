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
    centerss = list()
    for raw_line in conn:
        if raw_line[0:2] == '--':
            break
        point = raw_line.strip().split(' ')
        float_point = [float(i) for i in point]
        centerss.append(float_point)
    for raw_line in conn:
        point = raw_line.strip().split(' ')
        float_point = [float(i) for i in point]
        point_sett.append(float_point)
    return kk, mm, centerss, point_sett


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    with open('dataset_10927_3.txt', 'r') as f:
        k, m, centers, point_set = interpreter(f)
    d = 0.0
    for point in point_set:
        d += (dist_set(point, centers))**2
    d /= len(point_set)
    print(d)