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
            node['_e'].remove(i)
            if not node['_e']:
                del node['_e']
            node[letter] = {'_e': [i+1]}
            update_edges(index+1, node[letter])
            return None
    node['_e'].append(index)
    return None

def edge_len(node):
    l = 0
    for key, value in node.items():
        if key == '_e':
            l += len(node['_e'])
        else:
            l += 1
    return l


def tree_reducer(root_node):
    """Tree_reducer
    Reduces all non branching paths to multiple letter paths
    Does NOT work so far"""
    for key, value in list(root_node.items()):
        if key in ['A', 'C', 'G', 'T', ]:
            if edge_len(value) >= 2:
                tree_reducer(value)
            if edge_len(value) == 1:
                text = key
                current = value
                while edge_len(current) == 1 and '_e' not in current.keys():
                    current = list(current.values())[0]
                    text += list(current.keys())[0]
                del root_node[key]
                root_node[text] = current
                tree_reducer(current)
    return None

def tree_printer(root_node, conn):
    for key, value in root_node.items():
        if key == '_e':
            for index in value:
                conn.write(genome[index:]+'\n')
        else:
            conn.write(key+'\n')
            tree_printer(value, conn)
    return None


if __name__ == '__main__':
    os.chdir('C:\\Users\\Jacques\\Downloads')
    with open('dataset_294_8.txt', 'r') as f:
        genome = f.readline()
    suffix_tree = suffix_tree_builder(genome)
    with open('suffix_out.txt', 'w') as g:
        tree_printer(suffix_tree, g)

