"""
Compare performance of Dijkstra, bidirectional Dijkstra, A* algorithm,
and Bellman-Ford, using a N * N square where roads are all vertical and
all horizontal lines.

/!\ need to change A-star distance
a-star - show path.py
bidirectional a-star - show path.py
to use Euclidian distance
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

print("creating", N, "by", N, "map...")
nodes = {}
graph = {}
for i in range(N):
    for j in range(N):
        nodes[(i,j)] = (i, j)
        graph[(i,j)] = {}

for i in range(N):
    for j in range(N):
        if i > 0:
            graph[(i,j)][(i-1,j)] = 1
        if i < N-1:
            graph[(i,j)][(i+1,j)] = 1
        if j > 0:
            graph[(i,j)][(i,j-1)] = 1
        if j < N-1:
            graph[(i,j)][(i,j+1)] = 1
        
print("done")

t0 = time()
graph_rev = reverse(nodes, graph)
print("reversing graph in time =", "{0:.3f}".format(time() - t0))

source = (N/4, N/4)
destination = (3*N/4, 3*N/4)
print()
print("computing distance from", source, "to", destination)

print()
print("Dijkstra - show path")
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra - show path.py")
t0 = time()
dist_ref, parents = dijkstra.dijkstra(graph, source, destination)
print("distance =", dist_ref)
print("time     =", "{0:.3f}".format(time() - t0))

print()
print("Dijkstra")
dijkstra = imp.load_source("dijkstra", DIR + "dijkstra.py")
t0 = time()
dist = dijkstra.dijkstra(graph, source, destination)
if dist != dist_ref:
    print("################### !!!")
    print("distance =", dist)
print("time     =", "{0:.3f}".format(time() - t0))

print()
print("bidirectional Dijkstra - show path")
dijkstra = imp.load_source("bi_dijkstra", DIR + "bidirectional dijkstra - show path.py")
t0 = time()
dist, path = dijkstra.bi_dijkstra(nodes, graph, source, destination, graph_rev)
if dist != dist_ref:
    print("################### !!!")
    print("distance =", dist)
print("time     =", "{0:.3f}".format(time() - t0))

print()
print("A star - show path")
a_star = imp.load_source("a_star", DIR + "a-star - show path.py")
a_star.set_distance("euclid")
t0 = time()
dist, parents = a_star.a_star(nodes, graph, source, destination)
if dist != dist_ref:
    print("################### !!!")
    print("distance =", dist)
print("time     =", "{0:.3f}".format(time() - t0))

print()
print("bidirectional A star - show path")
bi_a_star = imp.load_source("bi_a_star", DIR + "bidirectional a-star - show path.py")
bi_a_star.set_distance("euclid")
t0 = time()
dist, parents = bi_a_star.bi_a_star(nodes, graph, source, destination, graph_rev)
print("distance =", dist)
print("time     =", "{0:.3f}".format(time() - t0))

print()
print("Bellman-Ford")
bellman_ford = imp.load_source("bellman_ford", DIR + "bellman_ford.py")
t0 = time()
BF = bellman_ford.bellman_ford(graph, source)
if dist != dist_ref:
    print("################### !!!")
    print("distance =", BF[0][destination])
print("time     =", "{0:.3f}".format(time() - t0))
