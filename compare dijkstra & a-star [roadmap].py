"""
Compare performance of Dijkstra, bidirectional Dijkstra, and A* algorithm
using a test map from http://www.dis.uniroma1.it/challenge9/download.shtml
"""

from time import time
import random

def reverse(nodes, graph):
    rev = {}
    for node in nodes:
        rev[node] = {}
    for node1 in graph:
        for node2 in graph[node1]:
            rev[node2][node1] = graph[node1][node2]
    return rev

import imp
# path to the python utility directory
DIR = "D:/Users/ARNAUD/Python/_Program library/"

# MAP = from http://www.dis.uniroma1.it/challenge9/download.shtml
# download & unzip MAP.gr (graph) and MAP.co (coordinates of nodes)
MAP = "USA-road-d.NE"
t0 = time()
print "reading map..."
graph = {}
with open(MAP + ".gr") as f:
    for line in f:
        content = line.split(' ')
        if content[0] == 'a':
            n1, n2, d = int(content[1]), int(content[2]), int(content[3])
            if n1 not in graph: graph[n1] = {}
            graph[n1][n2] = d
        elif content[0] == 'p':
            sp, N, M = content[1], int(content[2]), int(content[3])
            nodes = range(1, N+1)

nodes = {}
# computes coordinates of nodes for A* ...
with open(MAP + ".co") as f:
    for line in f:
        content = line.split(' ')
        if content[0] == 'v':
            n, longitude, latitude = int(content[1]), int(content[2]), int(content[3])
            nodes[n] = (longitude/1000000., latitude/1000000.)

print "done in time =", "{0:.3f}".format(time() - t0)

t0 = time()
graph_rev = reverse(nodes, graph)
print "reversing graph in time =", "{0:.3f}".format(time() - t0)

total1, error1 = 0., []
total2, error2 = 0., []
total3, error3 = 0., []
total4, error4 = 0., []
total5, error5 = 0., []

N_TEST = 10
for test in xrange(N_TEST):
    
    source = random.randrange(1, N)
    destination = random.randrange(1, N)
    
    print
    print "============================================"
    print "TEST NUMBER", test + 1
    print "computing distance from", source, "to", destination
    print "source     ", nodes[source]
    print "destination", nodes[destination]

    print
    print "Dijkstra"
    dijkstra = imp.load_source("dijkstra", DIR + "dijkstra.py")
    t0 = time()
    dist_ref = dijkstra.dijkstra(graph, source, destination)
    t0 = time() - t0
    print "distance =", dist_ref
    print "time     =", "{0:.3f}".format(t0)
    total1 += t0

    print
    print "Dijkstra - show path"
    dijkstra = imp.load_source("dijkstra", DIR + "dijkstra - show path.py")
    t0 = time()
    dist, parents = dijkstra.dijkstra(graph, source, destination)
    t0 = time() - t0
    if dist != dist_ref:
        print "distance =", dist
        print "################### !!!"
        error2.append(abs(dist - dist_ref))
    print "time     =", "{0:.3f}".format(t0)
    total2 += t0

    print
    print "bidirectional Dijkstra - show path"
    dijkstra = imp.load_source("bi_dijkstra", DIR + "bidirectional dijkstra - show path.py")
    t0 = time()
    dist, path = dijkstra.bi_dijkstra(nodes, graph, source, destination, graph_rev)
    t0 = time() - t0
    if dist != dist_ref:
        print "distance =", dist
        print "################### !!!"
        error3.append(abs(dist - dist_ref))
    print "time     =", "{0:.3f}".format(t0)
    total3 += t0

    print
    print "A star - show path"
    a_star = imp.load_source("a_star", DIR + "a-star - show path.py")
    t0 = time()
    dist, parents = a_star.a_star(nodes, graph, source, destination)
    t0 = time() - t0
    if dist != dist_ref:
        print "distance =", dist
        print "################### !!!"
        error4.append(abs(dist - dist_ref))
    print "time     =", "{0:.3f}".format(t0)
    total4 += t0

    print
    print "bidirectional A star - show path"
    bi_a_star = imp.load_source("bi_a_star", DIR + "bidirectional a-star - show path.py")
    t0 = time()
    dist, parents = bi_a_star.bi_a_star(nodes, graph, source, destination, graph_rev)
    t0 = time() - t0
    if dist != dist_ref:
        print "distance =", dist
        print "################### !!!"
        error5.append(abs(dist - dist_ref))
    print "time     =", "{0:.3f}".format(t0)
    total5 += t0

    """
    # BF is very time consuming on a road graph
    print
    print "Bellman-Ford"
    bellman_ford = imp.load_source("bellman_ford", DIR + "bellman_ford.py")
    t0 = time()
    BF = bellman_ford.bellman_ford(graph, source)
    print "distance =", BF[0]
    if BF[0] != dist_ref: print "################### !!!"
    print "time     =", "{0:.3f}".format(time() - t0)
    """

print
print "============================================"
print "Time for", N_TEST, "calculations ( [errors] ):"
print
print "Dijkstra                          ", "{0:.3f}".format(total1), " (", error1, ")"
print "Dijkstra - show path              ", "{0:.3f}".format(total2), " (", error2, ")"
print "bidirectional Dijkstra - show path", "{0:.3f}".format(total3), " (", error3, ")"
print "A star - show path                ", "{0:.3f}".format(total4), " (", error4, ")"
print "bidirectional A star - show path  ", "{0:.3f}".format(total5), " (", error5, ")"
