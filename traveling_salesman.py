"""
Traveling salesman

Computes the shortest path between all nodes of a connected graph
starting at one particular node and returning at that same node
(connected = there is a path between every pair of nodes)

dynamic programming algorithm
"""
import math
import itertools

def ts(points, graph):
    # calculate all distances
    distances = [[graph[x][y] for y in points] for x in points]
    # initial value = distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, i + 1]), i + 1): (dist, [0, i + 1]) for i, dist in enumerate(distances[0][1:])}
    n = len(points)
    for m in range(2, n):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
            for j in S - {0}:
                B[(S, j)] = min([(A[(S - {j}, k)][0] + distances[k][j], A[(S - {j},k)][1] + [j]) for k in S if (k != 0 and k != j)])
        A = B
    return min([(A[d][0] + distances[0][d[1]], A[d][1]) for d in iter(A)])


############################
# Example of use

if __name__ == "__main__":
    
    # a simple graph
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    coordinates = {}
    coordinates['a'] = [0., 0.]   #  b . . . . c
    coordinates['b'] = [0., 5.]   #  . . . . g .
    coordinates['c'] = [5., 5.]   #  . . h . . .
    coordinates['d'] = [5., 0.]   #  . e . . . .
    coordinates['e'] = [1., 2.]   #  . . . f . .
    coordinates['f'] = [3., 1.]   #  a i . . . d
    coordinates['g'] = [4., 4.]
    coordinates['h'] = [2., 3.]
    coordinates['i'] = [0., 1.] 

    def distance(p1, p2):
        """
        return crow (Euclidian) distance between p1 and p2
        p1 = [x1, y1]
        p2 = [x2, y2]
        use '0. +' to make sure expression is a float if int were used
        """
        return math.sqrt(0. + (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    # calculate all distances
    graph = {}
    for x in nodes:
        graph[x] = {}
        for y in nodes:
            graph[x][y] = distance(coordinates[x], coordinates[y])

    # re-arrange nodes list to start at any required node
    start = 'a'
    assert start in nodes
    new_nodes = list(nodes)
    new_nodes.remove(start)
    new_nodes = [start] + new_nodes

    # calculate traveling salesman solution
    result = ts(new_nodes, graph)
    distance = result[0]
    path = [new_nodes[x] for x in result[1]] + [new_nodes[0]]

    print()
    print(" -> ".join(path))
    print(distance)

    # sanity check:
    L = 0.
    for i in range(len(path)-1):
        L = L + graph[path[i]][path[i+1]]
    print(L)
    assert distance == L
    print()
