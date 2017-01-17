"""
Compare performance of Dijkstra, bidirectional Dijkstra, A* algorithm,
and Bellman-Ford, using a N * N square where roads are all vertical and
all horizontal lines.
"""

from time import time

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

# map = N * N square, roads are all vertical and all horizontal lines

N = 200

print "creating", N, "by", N, "map..."
nodes = {}
graph = {}
for i in xrange(N):
    for j in xrange(N):
        nodes[(i,j)] = (i, j)
        graph[(i,j)] = {}

for i in xrange(N):
    for j in xrange(N):
        if i > 0:
            graph[(i,j)][(i-1,j)] = 1
        if i < N-1:
            graph[(i,j)][(i+1,j)] = 1
        if j > 0:
            graph[(i,j)][(i,j-1)] = 1
        if j < N-1:
            graph[(i,j)][(i,j+1)] = 1
        
print "done"

t0 = time()
graph_rev = reverse(nodes, graph)
print "reversing graph in time =", "{0:.3f}".format(time() - t0)

source = (N/4, N/4)
destination = (3*N/4, 3*N/4)
print
print "computing distance from", source, "to", destination

print
print "Dijkstra - show path"
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra - show path.py")
t0 = time()
dist_ref, parents = dijkstra.dijkstra(graph, source, destination)
print "distance =", dist_ref
print "time     =", "{0:.3f}".format(time() - t0)

print
print "Dijkstra"
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra.py")
t0 = time()
dist = dijkstra.dijkstra(graph, source, destination)
assert dist == dist_ref
print "time     =", "{0:.3f}".format(time() - t0)

print
print "bidirectional Dijkstra - show path"
dijkstra = imp.load_source("bi_dijkstra", DIR + "bidirectional dijkstra - show path.py")
t0 = time()
dist, path = dijkstra.bi_dijkstra(nodes, graph, source, destination, graph_rev)
assert dist == dist_ref
print "time     =", "{0:.3f}".format(time() - t0)

print
print "A star - show path"
a_star = imp.load_source("a_star", DIR + "a-star - show path.py")
t0 = time()
dist, parents = a_star.a_star(nodes, graph, source, destination)
assert dist == dist_ref
print "time     =", "{0:.3f}".format(time() - t0)

print
print "bidirectional A star - show path"
bi_a_star = imp.load_source("bi_a_star", DIR + "bidirectional a-star - show path.py")
t0 = time()
dist, parents = bi_a_star.bi_a_star(nodes, graph, source, destination, graph_rev)
assert dist == dist_ref
print "time     =", "{0:.3f}".format(time() - t0)

print
print "Bellman-Ford"
bellman_ford = imp.load_source("bellman_ford", DIR + "bellman_ford.py")
t0 = time()
BF = bellman_ford.bellman_ford(graph, source)
assert BF[0][destination] == dist_ref
print "time     =", "{0:.3f}".format(time() - t0)


"""
N = 100
omputing distance from (25, 25) to (75, 75)

Dijkstra - show path
distance = 100
time     = 0.039

Dijkstra
time     = 0.034

bidirectional Dijkstra - show path
reversing graph in time = 0.022
time     = 0.032

A star - show path
time     = 0.019

bidirectional A star - show path
reversing graph in time = 0.023
time     = 0.028

Bellman-Ford
time     = 1.211

--------

N = 1000
computing distance from (250, 250) to (750, 750)

Dijkstra - show path
distance = 1000
time     = 5.484

Dijkstra
time     = 5.280

bidirectional Dijkstra - show path
reversing graph in time = 4.071
time     = 5.170

A star - show path
time     = 2.530

bidirectional A star - show path
reversing graph in time = 4.179
time     = 3.961

Bellman-Ford
time     = 1754.418 (or just under 30 minutes)
"""
