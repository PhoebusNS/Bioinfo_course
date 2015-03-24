__author__ = 'Jacques'

import os


def suffix_tree_builder(text):
    """Suffix_tree_builder
    Tries to insert every suffix from genome, from smaller to bigger as far as possible in the tree.
    When encountering a node that does not contain the current letter,
    exits to update edges to test whether a new node can be added."""
    n = len(text)
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
            node[letter] = {'_e': [i+1]}
            update_edges(index+1, node[letter])
            return None
    node['_e'].append(index)
    return None


def tree_reducer(tree):
    """Tree_reducer
    Reduces all non branching paths to multiple letter paths"""
    


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    f = open('dataset_294_8.txt', 'r')
    genome = f.readline() + '$'
    suffix_tree = suffix_tree_builder(genome)
