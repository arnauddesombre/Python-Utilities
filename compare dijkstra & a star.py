from time import time

import imp
# path to the python utility directory
DIR = "C:/Python/Utility/"

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
print "computing distance from ", source, "to", destination

print
print "Dijkstra - show path"
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra - show path.py")
t0 = time()
dist, parents = dijkstra.dijkstra(graph, source, destination)
print "distance =", dist[destination]
print "time     =", time() - t0

print
print "Dijkstra"
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra.py")
t0 = time()
dist = dijkstra.dijkstra(graph, source, destination)
print "distance =", dist[destination]
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
computing distance from  (25, 25) to (75, 75)

Dijkstra - show path
time     = 0.038

Dijkstra
time     = 0.037

A star
time     = 0.024

Bellman-Ford
time     = 1.149

--------

N = 1000
computing distance from  (250, 250) to (750, 750)

Dijkstra - show path
time     = 5.504

Dijkstra
time     = 5.394

A star
time     = 2.672

Bellman-Ford
time     = 1754.418 (that's just under 30 minutes)
"""
