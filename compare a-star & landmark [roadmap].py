"""
Compare performance of A* and Landmarks algorithm
using a test map from http://www.dis.uniroma1.it/challenge9/download.shtml
"""

from time import time
import random
import imp

# path to the python utility directory
DIR = "D:/Users/ARNAUD/Python/_Program library/"

def reverse(nodes, graph):
    rev = {}
    for node in nodes:
        rev[node] = {}
    for node1 in graph:
        for node2 in graph[node1]:
            rev[node2][node1] = graph[node1][node2]
    return rev

# MAP = from http://www.dis.uniroma1.it/challenge9/download.shtml
# download & unzip MAP.gr (graph) and MAP.co (coordinates of nodes)
MAP = "USA-road-d.NY"
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

t0 = time()
print "select landmarks"
top = -float("inf")
bottom = float("inf")
left = float("inf")
right = -float("inf")
for node in nodes:
    if nodes[node][0] < left:   left = nodes[node][0]
    if nodes[node][0] > right:  right = nodes[node][0]
    if nodes[node][1] < bottom: bottom = nodes[node][1]
    if nodes[node][1] > top:    top = nodes[node][1]
# 8 points: 4 corners + 4 center of each side
corners  = [(left, top), (right, top), (right, bottom), (left, bottom)]
centers  = [((left+right)/2., top), (right, (bottom+top)/2.), ((left+right)/2., bottom), (left, (bottom+top)/2.)]
points = corners + centers
# find 8 landmarks on the graph: the 8 nodes closest to the 8 points
distances = [float("inf")] * len(points)
landmarks = [None] * len(points)
a_star = imp.load_source("", DIR + "a-star.py")
for node in nodes:
    dist = [a_star._distance(nodes[node], points[i]) for i in xrange(len(points))]
    for i in xrange(len(landmarks)):
        if dist[i] < distances[i]:
            distances[i] = dist[i]
            landmarks[i] = node
print "done in time =", "{0:.3f}".format(time() - t0)    

print
print "compute all distances from landmarks"
dijkstra = imp.load_source("", DIR + "dijkstra.py")
t0 = time()
# node was (x,y) and will become (x,y, dist1a, dist1b, ..., distNa, distNb) where
# distIa is the distance from landmark I to node
# distIb is the distance from node to landmark I
# Note: the dataset provided for the 9th DIMACS Implementation Challenge
#        (from http://www.dis.uniroma1.it/challenge9/download.shtml) are symmetrical
#        so the d(node, landmark) = d(landmark, node)
for node in nodes:
    nodes[node] = list(nodes[node]) + [0] * 2 * len(landmarks)
for i in xrange(len(landmarks)):
    print i+1, "of", len(landmarks)
    # computes distance from landmark[i] to all nodes
    A = dijkstra.dijkstra(graph, landmarks[i])
    for node in nodes:
        nodes[node][2+2*i] = A[node]
    # computes distance from all nodes to landmark[i]
    A = dijkstra.dijkstra(graph_rev, landmarks[i])
    for node in nodes:
        nodes[node][2+2*i+1] = A[node]
for node in nodes:
    nodes[node] = tuple(nodes[node])
print "done in time =", "{0:.3f}".format(time() - t0)

total1, error1 = 0., []
total2, error2 = 0., []

N_TEST = 100
for test in xrange(N_TEST):
    
    source = random.randrange(1, N)
    destination = random.randrange(1, N)
    
    print
    print "============================================"
    print "TEST NUMBER", test + 1
    print "computing distance from", source, "to", destination
    print "source     ", nodes[source][:2]
    print "destination", nodes[destination][:2]

    print
    print "A star - show path"
    a_star = imp.load_source("a_star", DIR + "a-star - show path.py")
    t0 = time()
    dist_ref, parents = a_star.a_star(nodes, graph, source, destination)
    t0 = time() - t0
    print "distance =", dist_ref
    print "time     =", "{0:.3f}".format(t0)
    total1 += t0

    print
    print "landmark - show path"
    landmark = imp.load_source("landmark", DIR + "landmark - show path.py")
    t0 = time()
    dist, parents = landmark.landmark(nodes, graph, source, destination, len(landmarks))
    t0 = time() - t0
    if dist != dist_ref:
        print "distance =", dist
        print "################### !!!"
        error2.append(abs(dist - dist_ref))
    print "time     =", "{0:.3f}".format(t0)
    total2 += t0

print
print "============================================"
print "Time for", N_TEST, "calculations ( [errors] ):"
print
print "A star - show path    ", "{0:.3f}".format(total1), " (", error1, ")"
print "landmarks - show path ", "{0:.3f}".format(total2), " (", error2, ")"


"""
USING 8 LANDMARKS
(4 corners + 4 middle of sides)

results using USA-road-d.NY
---------------------------

reading map...
done in time = 3.854
reversing graph in time = 0.222
select landmarks
done in time = 3.302
compute all distances from landmarks
done in time = 12.827

Time for 1000 calculations ( [errors] ):
A star - show path     166.986  ( [] )
landmarks - show path  125.658  ( [1, 1] )
(33% improvement)

results using USA-road-d.NE
---------------------------

reading map...
done in time = 21.608
reversing graph in time = 1.697
select landmarks
done in time = 19.029
compute all distances from landmarks
done in time = 76.461

Time for 1000 calculations ( [errors] ):
A star - show path     1134.748  ( [] )
landmarks - show path  825.231  ( [] )
(37% improvement)

/!\ This is only an average improvement;
    in some cases Landmark is worse by more than 100%

"""
