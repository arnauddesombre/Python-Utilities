"""
Find all simple paths (no loop) in a
directed graph starting from a specified
node by brute recursive enumeration

Variant:
find only one
"""
import sys
sys.setrecursionlimit(1000000)

# define graph as a global variable, could otherwise be:
# def find_all_paths(graph, start, end, path=[]):
# def find_path(graph, start, end, path=[]):
graph = {}

def find_all_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_path(start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(node, end, path)
            if newpath:
                return newpath
    return None


############################
#        E
#       / \
#     4/   \4
#     D--3--C
#     |     |
#     2     2
#     |     |
#     A--1--B
#

if __name__ == "__main__":
    
    nodes = set(['A', 'B', 'C', 'D', 'E'])
    graph = {'A': {'B':1, 'D':2},
             'B': {'A':1, 'C':2},
             'C': {'B':2, 'D':3, 'E':4},
             'D': {'A':2, 'C':3, 'E':4},
             'E': {'C':4, 'D':4}}

    print
    print find_all_paths('A', 'E')
    print
    print find_path('A', 'E')
    print
