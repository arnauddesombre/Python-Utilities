"""
compute the shortest distance from a source to a destination
in a directed graph where some crow distance (Euclid) can be
defined, and where distances from landmarks are known,
as well as the shortest corresponding path
/!\ all distances must be >= 0

return:
distance = length of shortest path
path = shortest path from source to destination

Note that some pre-processing is necessary:
distance from all landmarks to all nodes is required
distance from all nodes to all landmarks is required
"""
from heapq import heappush, heappop

def landmark(nodes, graph, source, destination, n_landmark=None):
    # nodes is a list of tuples
    # (longitude, latitude, dist(1,1), dist(1,2),..., dist(n_landmark,1), dist(n_landmark,2))
    # longitude, latitude = coordinates of the node
    # dist(I,1) = distance (in the graph) from landmark I to the node (FROM landmark)
    # dist(I,2) = distance (in the graph) from the node to landmark I (TO landmark)
    # (dist(I,1) and dist(I,2) are not necessarily equal)
    # if n_landmark == 0, this is Dijkstra
    if n_landmark == None:
        n_landmark = (len(node) - 2) / 2
    visited = {}
    parents = {}
    queue = [(0, 0, source, None)]
    distance = float("inf")
    while queue:
        path_estimate, path_len, v, parent = heappop(queue)
        if v not in visited:
            visited[v] = True
            parents[v] = parent
            if v == destination:
                distance = path_len
                break
            for w, edge_len in graph[v].items():
                if w not in visited:
                    d = path_len + edge_len
                    estimate = 0
                    for i in xrange(n_landmark): # enumerate distances from/to landmarks
                        estimate_i = nodes[destination][2+2*i] - nodes[w][2+2*i]
                        if estimate_i > estimate: estimate = estimate_i
                        estimate_i = nodes[w][2+2*i+1] - nodes[destination][2+2*i+1]
                        if estimate_i > estimate: estimate = estimate_i
                    estimate = d + estimate
                    heappush(queue, (estimate, d, w, v))
    return distance, landmark_path(parents, source, destination) if distance < float("inf") else []

def landmark_path(parents, source, destination):
    node = destination
    path = [node]
    while node != source:
        if node in parents:
            node = parents[node]
            path.append(node)
        else:
            return []
    return path[::-1]
