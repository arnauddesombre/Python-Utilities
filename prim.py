"""
Prim's MST (minimum spanning tree) algorithm

costs can be negative.
MST assumes the graph is undirected.

'graph' is defined as: graph = {from:{to:dist, ...}, ...}
if graph[from][to] == dist, it is assumed that graph[to][from] == dist as well
therefore in the MST, the edge could be [from, to, dist] or [to, from, dist]

/!\ if both graph[from][to] and graph[to][from] are defined, even with the same
value, it would be assumed that this creates 2 different edges between 'from' and 'to'
(which would have no impact on the output)
"""

from heapq import heappop, heappush, heapify
import random

def prim(nodes, graph):
    """
    input:   graph   = in dictionary form {from:{to:distance, ...}, ...}
             nodes   = list of all nodes
    output:  the MST = list of (head, tail, weight), True if MST otherwise False
    """
    edges = {}
    for node in nodes:
        edges[node] = []
    for n1 in graph:
        for n2 in graph[n1]:
            edges[n1].append((graph[n1][n2], n1, n2))
            edges[n2].append((graph[n1][n2], n2, n1))
    mst = []
    # node is a random node from the graph
    node = random.choice(list(graph.keys()))
    visited = {node:True}
    usable_edges = list(edges[node]) # deep copy
    heapify(usable_edges)
    while usable_edges:
        cost, n1, n2 = heappop(usable_edges)
        if n2 not in visited:
            visited[n2] = True
            mst.append((n1, n2, cost))
            for e in edges[n2]:
                if e[2] not in visited:
                    heappush(usable_edges, e)
    ok = True
    for node in nodes:
        if node not in visited:
            ok = False
            break
    return mst, ok


############################
#        E
#       / \
#     1/   \-1
#     D--3--C
#     |     |
#     2     3
#     |     |
#     A--1--B
#

if __name__ == "__main__":
    
    nodes = set(['A', 'B', 'C', 'D', 'E'])
    graph = {'A': {'B':1, 'D':2},
             'B': {'C':3},
             'C': {'D':3, 'E':-1},
             'D': {'E':1},
             'E': {}}

    print
    print(prim(nodes, graph))
    print
