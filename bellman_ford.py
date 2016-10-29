"""
Bellman-Ford algorithm

compute all shortest distances from source to all points
in graph aswell as the shortest corresponding paths
/!\ distances can be < 0
/!\ no negative cycle

return:
d = shortest distances
d[node] is the shortest distance from source to node
p = shortest path parents dictionary
p[node] is the parent of node in the shortest path from the given source
"""

def relax(u, v, graph, d, p):
    if d[v] > d[u] + graph[u][v]:
        d[v] = d[u] + graph[u][v]
        p[v] = u

def bellman_ford(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    for i in xrange(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for u in graph:
        for v in graph[u]:
            # test for no negative cycle
            assert d[v] <= d[u] + graph[u][v]
    return d, p

def bellman_ford_path(parents, source, destination):
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
#     1/   \-1 for E->C and +2 for C->E
#     D--3--C
#     |     |
#     2     3
#     |     |
#     A--1--B
#

nodes = set(['A', 'B', 'C', 'D', 'E'])
graph = {'A': {'B':1, 'D':2},
         'B': {'A':1, 'C':3},
         'C': {'B':3, 'D':3, 'E':2},
         'D': {'A':2, 'C':3, 'E':1},
         'E': {'C':-1, 'D':1}}

A, parents = bellman_ford(graph, 'A')

print
print A
print
print bellman_ford_path(parents, 'A', 'C')
print
