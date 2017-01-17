"""
Compare performance of Dijkstra, bidirectional Dijkstra, A* algorithm,
and Bellman-Ford, using a N * N square where roads are all vertical and
all horizontal lines.
"""

from time import time

import imp
# path to the python utility directory
DIR = "D:/Users/ARNAUD/Python/_Program library/"

# map = N * N square, roads are all vertical and all horizontal lines

N = 100

print "creating", N, "by", N, "map..."
nodes = {}
graph = {}
for i in xrange(N):
    for j in xrange(N):
        nodes[(i,j)] = (i, j)
        graph[(i,j)] = {}

for i in xrange(N):
    for j in xrange(N):
        if i > 0:   graph[(i,j)][(i-1,j)] = 1
        if i < N-1: graph[(i,j)][(i+1,j)] = 1
        if j > 0:   graph[(i,j)][(i,j-1)] = 1
        if j < N-1: graph[(i,j)][(i,j+1)] = 1
        
print "done"


source = (N/4, N/4)
destination = (3*N/4, 3*N/4)
print
print "computing distance from", source, "to", destination

print
print "Dijkstra - show path"
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra - show path.py")
t0 = time()
dist, parents = dijkstra.dijkstra(graph, source, destination)
print "distance =", dist
print "time     =", time() - t0

print
print "Dijkstra"
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra.py")
t0 = time()
dist = dijkstra.dijkstra(graph, source, destination)
print "distance =", dist
print "time     =", time() - t0

print
print "bidirectional Dijkstra - show path"
dijkstra = imp.load_source("bi_dijkstra", DIR + "bidirectional dijkstra - show path.py")
t0 = time()
graph_rev = dijkstra.reverse(nodes, graph)
print "reversing graph in time =", time() - t0
t0 = time()
dist, path = dijkstra.bi_dijkstra(nodes, graph, source, destination, graph_rev)
print "distance =", dist
print "time     =", time() - t0

print
print "A star"
a_star = imp.load_source("a_star", DIR + "a-star - show path.py")
t0 = time()
dist, parents = a_star.a_star(nodes, graph, source, destination)
print "distance =", dist
print "time     =", time() - t0

print
print "Bellman-Ford"
bellman_ford = imp.load_source("bellman_ford", DIR + "bellman_ford.py")
t0 = time()
BF = bellman_ford.bellman_ford(graph, source)
print "distance =", BF[0][destination]
print "time     =", time() - t0


"""
N = 100
computing distance from (25, 25) to (75, 75)

Dijkstra - show path
time     = 0.039

Dijkstra
time     = 0.036

bidirectional Dijkstra - show path
reversing graph in time = 0.022
time     = 0.035

A star
time     = 0.022

Bellman-Ford
time     = 1.213

--------

N = 1000
computing distance from  (250, 250) to (750, 750)

Dijkstra - show path
time     = 5.393

Dijkstra
time     = 5.394

bidirectional Dijkstra - show path
reversing graph in time = 4.088
time     = 5.294

A star
time     = 2.557

Bellman-Ford
time     = 1754.418 (or just under 30 minutes)
"""
