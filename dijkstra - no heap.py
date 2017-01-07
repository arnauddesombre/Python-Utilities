"""
compute all shortest distances from source to all points in graph
/!\ all distances must be >= 0

return:
A = shortest distances
A[node] is the shortest distance from source to node
"""
def dijkstra(graph, source):
    X = [source]
    A = {}
    A[source] = 0
    edges = [(source, w) for w in graph[source]]
    while edges != []:
        greedyCriteria = float("inf")
        greedyNode = 0
        for n in edges:
            d = A[n[0]] + graph[n[0]][n[1]]
            if d < greedyCriteria:
                greedyCriteria = d
                greedyNode = n
        X.append(greedyNode[1])
        A[greedyNode[1]] = greedyCriteria
        edges = [n for n in edges if n[1] != greedyNode[1]]
        edges = edges + [(greedyNode[1], w) for w in graph[greedyNode[1]] if w not in X]
    return A

"""
note:
this algorithm cannot stop early if a particular
targetted destination has been reached because it
isn't implemented with heap. The distance found
would be incorrect.
"""


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
