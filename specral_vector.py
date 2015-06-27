__author__ = 'Jacques'

from os import chdir
from operator import itemgetter

class Node(object):
    def __init__(self, index):
        self.index = index
        self.weight = 0
        self.ancestor = 'source'

    def calculate_weight(self, own, ref):
        poss_anc = []
        for i in weights:
            if i > self.index:
                poss_anc.append((float('-inf'), 'no'))
            else:
                parent = self.index - i
                w = own + ref[parent].weight
                poss_anc.append((w, parent))
        anc = max(poss_anc, key=itemgetter(0))
        self.weight = anc[0]
        self.ancestor = anc[1]


def graph_builder(spec):
    graph = list()
    graph.append(Node(0))
    for i in range(1, len(spec)+1):
        new = Node(i)
        new.calculate_weight(spec[i-1], graph)
        graph.append(new)
    return graph


if __name__ == '__main__':
    chdir('C:\\Users\\Jacques\\Downloads')
    with open('integer_mass_table.txt') as e:
        mass_to_amino = dict()
        amino_to_mass = dict()
        for item in e:
            temp = item.strip().split(' ')
            try:
                mass_to_amino[int(temp[1])] = temp[0]
                amino_to_mass[temp[0]] = int(temp[1])
            except IndexError:
                pass
        weights = mass_to_amino.keys()

    with open('dataset_11813_10.txt', 'r') as f:
        spectral = f.readline().strip().split(' ')
        spectral = [float(x) for x in spectral]

    f_graph = graph_builder(spectral)
    peptide = ''
    node = f_graph[-1]
    while True:
        anc = node.ancestor
        if anc == 'source':
            break
        if anc == 'no':
            print('Error')
            break
        peptide += mass_to_amino[node.index - anc]
        node = f_graph[anc]
    out = peptide[::-1]
    print(out)
