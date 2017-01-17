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
from math import sqrt

def euclid(x, y):
    # example of distance function
    # x and y = in coordinate format = (i,j)
    # 'return 0' <=> Dijkstra algorithm
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

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
    best_distance = float("inf")
    visited_nodes = []
    while queue or queue_rev:
        node10, node11 = None, None
        node20, node21 = None, None
        # process queue
        if queue:
            path_estimate, path_len1, v1, parent = heappop(queue)
            if v1 not in dist: # v1 is not visited
                node10 = v1
                visited_nodes.append(v1)
                dist[v1] = path_len1
                parents[v1] = parent
                for w, edge_len in graph[v1].items():
                    if w not in dist:
                        d = path_len1 + edge_len
                        estimate = d + (euclid(nodes[w], nodes[destination]) - euclid(nodes[w], nodes[source])) / 2.
                        heappush(queue, (estimate, d, w, v1))
                        if w in dist_rev:
                            if d + dist_rev[w] < best_distance:
                                best_distance = d + dist_rev[w]
                                node11 = w
        # process queue_rev
        if queue_rev:
            path_estimate, path_len2, v2, parent = heappop(queue_rev)
            if v2 not in dist_rev: # v2 is not visited
                node20 = v2
                visited_nodes.append(v2)
                dist_rev[v2] = path_len2
                parents_rev[v2] = parent
                for w, edge_len in graph_rev[v2].items():
                    if w not in dist_rev:
                        d = path_len2 + edge_len
                        estimate = d + (euclid(nodes[w], nodes[source]) - euclid(nodes[w], nodes[destination])) / 2.
                        heappush(queue_rev, (estimate, d, w, v2))
                        if w in dist:
                            if d + dist[w] < best_distance:
                                best_distance = d + dist[w]
                                node21 = w
        # stop criteria
        # from http://www.cs.princeton.edu/courses/archive/spr06/cos423/Handouts/EPP%20shortest%20path%20algorithms.pdf
        # page 16 (see page 9 for best path seen so far)
        if path_len1 + path_len2 >= best_distance:
            if node10 != None and node11 != None:
                parents[node11] = node10
                dist[node11] = dist[node10] + graph[node10][node11]
                visited_nodes.append(node11)
            if node20 != None and node21 != None:
                parents[node21] = node20
                dist[node21] = dist[node20] + graph_rev[node20][node21]
                visited_nodes.append(node21)
            break

    # process shortest path and shortest distance
    distance = float("inf")
    u_best = None
    for node in visited_nodes:
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
    dist, path = bi_a_star(nodes, graph, source, destination)

    print "distance =", dist
    print "path     =", path
    print
