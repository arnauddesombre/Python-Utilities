"""
Prim's MST (minimum spanning tree) algorithm

costs can be negative
MST assumes the graph is undirected.
'graph' is defined as: graph = {from:{to:dist, ...}, ...}
if graph[from][to] = dist, it is assumed that graph[to]from] = dist as well
therefore in the MST, the edge would be [from, to, dist] or [to, from, dits]
"""
from heapq import heappop, heappush, heapify
import random

def prim(graph):
    """
    input:   graph   = in dictionary form {from:{to:distance, ...}, ...}
    output:  the MST = list of (head, tail, weight)
    """
    conn = {}
    for n1 in graph:
        if n1 not in conn:
            conn[n1] = []
        for n2 in graph[n1]:
            if n2 not in conn:
                conn[n2] = []
            conn[n1].append((graph[n1][n2], n1, n2))
            conn[n2].append((graph[n1][n2], n2, n1))

    mst = []
    # node is a random node from the graph
    # it's actually a random tail node, but
    # it doesn't matter for the algorithm,
    # as any node would do
    node = random.choice(graph.keys())
    used = {node:True}
    usable_edges = conn[node][:]
    heapify(usable_edges)

    while usable_edges:
        cost, n1, n2 = heappop(usable_edges)
        if n2 not in used:
            used[n2] = True
            mst.append((n1, n2, cost))
            for e in conn[n2]:
                if e[2] not in used:
                    heappush(usable_edges, e)

    return mst


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
             'B': {'A':1, 'C':3},
             'C': {'B':3, 'D':3, 'E':-1},
             'D': {'A':2, 'C':3, 'E':1},
             'E': {'C':-1, 'D':1}}

    print
    print prim(graph)
    print
