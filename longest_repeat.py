__author__ = 'Jacques'

import os

current_max = 0
current_text = ''

def suffix_tree_builder(genome):
    """Suffix_tree_builder
    Tries to insert every suffix from genome, from smaller to bigger as far as possible in the tree.
    When encountering a node that does not contain the current letter,
    exits to update edges to test whether a new node can be added."""
    n = len(genome)
    root = dict()
    for i in range(n-1, -1, -1):
        current = root
        for j in range(i,n):
            if genome[j] in current:
                current = current[genome[j]]
            elif '_e' in current:
                update_edges(j,current)
                break
            else:
                current.setdefault('_e', list()).append(j)
                break
    return root


def update_edges(index, node):
    """Update_edges
    In a terminal node, check edges to see if any current edge starts with the same letter as the current index
    If yes, generates a new letter label with the reduced edge inside, and recursively tests edge start"""
    letter = genome[index]
    for i in node['_e']:
        if genome[i] == letter:
            node['_e'].remove(i)
            if not node['_e']:
                del node['_e']
            node[letter] = {'_e': [i+1]}
            update_edges(index+1, node[letter])
            return None
    node['_e'].append(index)
    return None

def repeat_finder(node, index, text):
    stop = True
    for key, value in node.items():
        if key in ['A', 'C', 'G', 'T']:
            repeat_finder(value, index+1, text+key)
            stop = False
    if stop:
        global current_max
        global current_text
        if index > current_max:
            current_max = index
            current_text = text
    return None


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    with open('dataset_296_5.txt', 'r') as f:
        genome = f.readline()+'$'
    suffix_tree = suffix_tree_builder(genome)
    repeat_finder(suffix_tree, 0, '')
    print(current_text)
