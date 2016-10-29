"""
compute all shortest distances from source to all points
in graph as well as the shortest corresponding paths
/!\ all distances must be >= 0

return:
A = shortest distances
A[node] is the shortest distance from source to node
parent = shortest path parents dictionary
parent[node] is the parent of node in the shortest path from the given source
"""
from heapq import heappush, heappop

def dijkstra(graph, source, destination=None):
    # algorithm stops if a specificied
    # destination has been reached
    A = {}
    parents = {}
    queue = [(0, source, None)]
    while queue:
        path_len, v, parent = heappop(queue)
        if v not in A: # v is not visited
            A[v] = path_len
            parents[v] = parent
            if v == destination:
                break
            for w, edge_len in graph[v].items():
                if w not in A:
                    heappush(queue, (path_len + edge_len, w, v))
    return A, parents

def dijkstra_path(parents, source, destination):
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
#     1/   \2
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
         'E': {'C':2, 'D':1}}

A, parents = dijkstra(graph, 'A')

print A
print
print dijkstra_path(parents, 'A', 'C')

