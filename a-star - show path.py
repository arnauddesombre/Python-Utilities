"""
compute the shortest distance from a source to a destination
in a directed graph where some crow distance (Euclid) can be
defined as well as the shortest corresponding path
/!\ all distances must be >= 0

return:
distance = length of shortest path
path = shortest path from source to destination
"""
from heapq import heappush, heappop
from math import sqrt

def euclid(x, y):
    # example of distance function
    # x and y = in coordinate format = (i,j)
    # 'return 0' <=> Dijkstra algorithm
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def a_star(nodes, graph, source, destination):
    visited = {}
    parents = {}
    estimate = euclid(nodes[source], nodes[destination])
    queue = [(estimate, 0, source, None)]
    distance = float("inf")
    while queue:
        path_estimate, path_len, v, parent = heappop(queue)
        if v not in visited:
            visited[v] = True
            parents[v] = parent
            if v == destination:
                distance = path_len
                break
            for w, edge_len in graph[v].items():
                if w not in visited:
                    d = path_len + edge_len
                    estimate = d + euclid(nodes[w], nodes[destination])
                    heappush(queue, (estimate, d, w, v))
    return distance, a_star_path(parents, source, destination) if distance < float("inf") else []

def a_star_path(parents, source, destination):
    node = destination
    path = [node]
    while node != source:
        if node in parents:
            node = parents[node]
            path.append(node)
        else:
            return []
    return path[::-1]


############################
#        E
#       / \
#     1/   \1
#     D--3--C
#     |     |
#     2     4
#     |     |
#     A--1--B
#

if __name__ == "__main__":
    
    nodes = {'A':(0,0),
             'B':(1,0),
             'C':(1,3),
             'D':(0,2),
             'E':(0.5,3)}
    graph = {'A': {'B':1, 'D':2},
             'B': {'A':1, 'C':4},
             'C': {'B':4, 'D':3, 'E':1},
             'D': {'A':2, 'C':3, 'E':1},
             'E': {'C':1, 'D':1}}

    source = 'A'
    destination = 'C'
    dist, path = a_star(nodes, graph, source, destination)

    print "distance =", dist
    print "path     =", path
    print
