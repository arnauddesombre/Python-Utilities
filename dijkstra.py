"""
compute all shortest distances from a source to all nodes in a directed graph
/!\ all distances must be >= 0

return:
if destination not specified:
  A = shortest distances; where A[node] is the shortest distance from source to node
if destination specified:
  shortest distance between 'source' and 'destination'
"""
from heapq import heappush, heappop

def dijkstra(graph, source, destination=None):
    # algorithm stops if a specificied
    # destination has been reached
    A = {}
    queue = [(0, source)]
    while queue:
        path_len, v = heappop(queue)
        if v not in A: # v is not visited
            A[v] = path_len
            if v == destination:
                break
            for w, edge_len in graph[v].items():
                if w not in A:
                    heappush(queue, (path_len + edge_len, w))
    if destination == None:
        # return all distances
        return A
    else:
        # only distance to 'destination' is correct
        if destination in A:
            return A[destination]
        else:
            return float("inf")
        


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

if __name__ == "__main__":
    
    nodes = set(['A', 'B', 'C', 'D', 'E'])
    graph = {'A': {'B':1, 'D':2},
             'B': {'A':1, 'C':3},
             'C': {'B':3, 'D':3, 'E':2},
             'D': {'A':2, 'C':3, 'E':1},
             'E': {'C':2, 'D':1}}

    print
    print dijkstra(graph, 'A')
    print
    print dijkstra(graph, 'A', 'C')
    print
