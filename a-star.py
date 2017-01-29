"""
compute the shortest distance from a source to a destination
in a directed graph where some crow distance (Euclid) can be
defined
/!\ all distances must be >= 0

return:
distance = length of shortest path
path = shortest path from source to destination
"""
from heapq import heappush, heappop
from math import sqrt, cos, asin

METHOD = "haversine"

def set_distance(method):
    global METHOD
    METHOD = method

def _distance(x, y):
    # example of distance function
    if METHOD == "haversine":
        return haversine(x[1], x[0], y[1], y[0])
    elif METHOD == "euclid":
        return euclid(x, y)
    else:
        # Dijkstra
        return 0

def euclid(x, y):
    # x and y = in coordinate format = (i,j)
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def haversine(lat1, lon1, lat2, lon2):
    # from:
    # https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    # http://www.movable-type.co.uk/scripts/latlong.html
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2. + cos(lat1 * p) * cos(lat2 * p) * (1. - cos((lon2 - lon1) * p)) / 2.
    # distance is in 0.1 meters (10 x distance is in meters)
    return 12742. * asin(sqrt(a)) * 10000.

def a_star(nodes, graph, source, destination):
    visited = {}
    estimate = _distance(nodes[source], nodes[destination])
    queue = [(estimate, 0, source)]
    distance = float("inf")
    while queue:
        path_estimate, path_len, v = heappop(queue)
        if v not in visited:
            visited[v] = True
            if v == destination:
                distance = path_len
                break
            for w, edge_len in graph[v].items():
                if w not in visited:
                    d = path_len + edge_len
                    estimate = d + _distance(nodes[w], nodes[destination])
                    heappush(queue, (estimate, d, w))
    return distance


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
    set_distance("euclid")
    dist = a_star(nodes, graph, source, destination)

    print "distance =", dist
    print
