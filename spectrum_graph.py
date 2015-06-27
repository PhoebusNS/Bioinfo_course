__author__ = 'Jacques'

from os import chdir


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child, acid):
        self.children[child] = acid


def interpreter(conn):
    tspec = conn.readline().strip().split(' ')
    tspecint = [int(x) for x in tspec]
    tspecint.insert(0, 0)
    return tspecint


def graph_build(spec, conn):
    graph = {i: Node(i) for i in spec}
    for i in spec:
        for j in spec:
            if i < j:
                diff = j-i
                if diff in amino:
                    conn.write(str(i)+'->'+str(j)+':'+amino[diff]+'\n')
                    graph[i].add_child(j, amino[diff])
    return graph

if __name__ == '__main__':
    chdir('C:\\Users\\Jacques\\Downloads')
    with open('integer_mass_table.txt') as e:
        amino = dict()
        for item in e:
            temp = item.strip().split(' ')
            try:
                amino[int(temp[1])] = temp[0]
            except IndexError:
                pass

    with open('dataset_11813_2.txt', 'r') as f:
        spectrum = interpreter(f)

    with open('graph_out.txt', 'w') as g:
        spec_graph = graph_build(spectrum, g)

#    for val, node in spec_graph.items():
#        print(val, node.value, node.children)
