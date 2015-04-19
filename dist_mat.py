__author__ = 'Jacques'

import os
from collections import defaultdict


def graph_builder(conn):
    """Graph_builder
    Takes a connection to a file with an adjacency list of a graph whose leaves are integers between 0 and n - 1
    n is given by the first line, other lines respect the notation a->b:c
    Means that node a is connected to node b by an edge of weight c
    Saved in a dictionary as a:(b,c)"""
    nn = int(conn.readline().strip())
    dd = defaultdict(list)
    for lin in conn:
        temp = lin.strip().split('->')
        a = int(temp[0])
        temp2 = temp[1].split(':')
        b = int(temp2[0])
        c = int(temp2[1])
        dd[a].append((b, c))
    return nn, dd


def paths_from(leaf):
    neighbour = d[leaf][0]  # Because each leaf has a single neighbour
    next_step(leaf, neighbour[0], neighbour[1], leaf)
    return None


def next_step(leaf, node, dist, prev):
    global dist_mat
    for b, c in d[node]:
        if b == prev:
            continue
        elif b < n:
            dist_mat[leaf][b] = c+dist
        else:
            next_step(leaf, b, c+dist, node)
    return None


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    with open('tree_out.txt', 'r') as f:
        n, d = graph_builder(f)
    dist_mat = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        paths_from(i)
    with open('matrix_out.txt', 'w') as g:
        for line in dist_mat:
            for i, item in enumerate(line):
                if i == n-1:
                    g.write(str(item)+'\n')
                else:
                    g.write(str(item)+' ')