#!/usr/bin/python2

from time import time

# map = N * N square, roads are all vertical and all horizontal lines

N = 1000

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

import imp
DIR = "D:/Users/ARNAUD/Python/_Program library/"
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra - heap - show path.py")
a_star = imp.load_source("a_star", DIR + "a-star - heap - show path.py")

source = (N/4,N/4)
destination = (3*N/4, 3*N/4)
print
print "computing distance from ", source, "to", destination

print
print "Dijkstra"
t0 = time()
dist, parents = dijkstra.dijkstra(graph, source, destination)
print "distance =", dist[destination]
print "time     =", time() - t0

print
print "A star"
t0 = time()
dist, parents = a_star.a_star(nodes, graph, source, destination)
print "distance =", dist
print "time     =", time() - t0
