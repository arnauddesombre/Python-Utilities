"""
compute the shortest distance from a source to a destination
in a directed graph  where some crow distance (Euclid) can be
defined as well as the shortest corresponding path using
bi-directional A* algorithm
/!\ all distances must be >= 0

return:
shortest distance
shortest path from 'source' to 'destination'
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
    p = 0.017453292519943295  # math.pi / 180
    a = 0.5 - cos((lat2 - lat1) * p)/2. + cos(lat1 * p) * cos(lat2 * p) * (1. - cos((lon2 - lon1) * p)) / 2.
    # distance is in 0.1 meters (10 distance is in meters)
    return 12742. * asin(sqrt(a)) * 10000. # // 12742 = 2 * R; R = 6371 km (earth radius)

def reverse(nodes, graph):
    rev = {}
    for node in nodes:
        rev[node] = {}
    for node1 in graph:
        for node2 in graph[node1]:
            rev[node2][node1] = graph[node1][node2]
    return rev

def bi_a_star(nodes, graph, source, destination, graph_rev=None):
    if graph_rev == None:
        graph_rev = reverse(nodes, graph)

    dist, dist_rev = {}, {}
    parents, parents_rev = {}, {}
    queue, queue_rev = [(0, 0, source, None)], [(0, 0, destination, None)]
    visited_nodes, visited_nodes_rev = {}, {}
    best_distance = float("inf")
    path_len1 = 0
    path_len2 = 0
    add_on = _distance(nodes[source], nodes[destination]) / 2.
    while queue or queue_rev:
        # process queue
        if queue:
            path_estimate, path_len1, v1, parent = heappop(queue)
            if v1 not in visited_nodes:
                visited_nodes[v1] = True
                dist[v1] = path_len1
                parents[v1] = parent
                for w, edge_len in graph[v1].items():
                    if w not in visited_nodes:
                        dist[w] = path_len1 + edge_len
                        parents[w] = v1
                        estimate = dist[w] + (_distance(nodes[w], nodes[destination]) - _distance(nodes[w], nodes[source])) / 2.
                        heappush(queue, (estimate, dist[w], w, v1))
                        if w in dist_rev:
                            if dist[w] + dist_rev[w] < best_distance:
                                best_distance = dist[w] + dist_rev[w]
        # process queue_rev
        if queue_rev:
            path_estimate, path_len2, v2, parent = heappop(queue_rev)
            if v2 not in visited_nodes_rev:
                visited_nodes_rev[v2] = True
                dist_rev[v2] = path_len2
                parents_rev[v2] = parent
                for w, edge_len in graph_rev[v2].items():
                    if w not in visited_nodes_rev:
                        dist_rev[w] = path_len2 + edge_len
                        parents_rev[w] = v2
                        estimate = dist_rev[w] + (_distance(nodes[w], nodes[source]) - _distance(nodes[w], nodes[destination])) / 2.
                        heappush(queue_rev, (estimate, dist_rev[w], w, v2))
                        if w in dist:
                            if dist_rev[w] + dist[w] < best_distance:
                                best_distance = dist_rev[w] + dist[w]
        # stop criteria
        # from http://www.cs.princeton.edu/courses/archive/spr06/cos423/Handouts/EPP%20shortest%20path%20algorithms.pdf
        # page 16 (see page 9 for best path seen so far)
        if path_len1 + path_len2 > best_distance + add_on:
            break

    # process shortest path and shortest distance
    distance = float("inf")
    u_best = None
    for node in visited_nodes.keys() + visited_nodes_rev.keys():
        if node in dist and node in dist_rev:
            if dist[node] + dist_rev[node] < distance:
                u_best = node
                distance = dist[node] + dist_rev[node]
    if distance == float("inf"):
        return distance, []

    path = []
    last = u_best
    while last != source:
        path.append(last)
        last = parents[last]
    path.append(source)
    path = path[::-1]
    last = u_best
    while last != destination:
        last = parents_rev[last]
        path.append(last)

    return distance, path


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
    dist, path = bi_a_star(nodes, graph, source, destination)

    print "distance =", dist
    print "path     =", path
    print
