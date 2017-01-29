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
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2. + cos(lat1 * p) * cos(lat2 * p) * (1. - cos((lon2 - lon1) * p)) / 2.
    # distance is in 0.1 meters (10 x distance is in meters)
    return 12742. * asin(sqrt(a)) * 10000.

def landmark(nodes, graph, source, destination, landmarks=None, n_landmark=None, optimize=True):
    # nodes is a list of tuples
    # (longitude, latitude, dist(1,1), dist(1,2),..., dist(n_landmark,1), dist(n_landmark,2))
    # longitude, latitude = coordinates of the node
    # dist(I,1) = distance (in the graph) from landmark I to the node (FROM landmark)
    # dist(I,2) = distance (in the graph) from the node to landmark I (TO landmark)
    # (dist(I,1) and dist(I,2) are not necessarily equal)
    # if landmarks == None, all landmarks are used
    # otherwise, landmarks is the list of nodes that are landmarks
    # if n_landmark == 0, this is Dijkstra
    if n_landmark == None:
        n_landmark = (len(nodes[source]) - 2) / 2
    if landmarks == None or not optimize:
        landmarks = xrange(n_landmark)
    elif optimize:
        landmarks = best_landmarks(nodes[source][:2], nodes[destination][:2], [nodes[x][:2] for x in landmarks], n_landmark)
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
                    for i in landmarks:
                        estimate_i = nodes[destination][2+2*i] - nodes[w][2+2*i]
                        if estimate_i > estimate: estimate = estimate_i
                        estimate_i = nodes[w][2+2*i+1] - nodes[destination][2+2*i+1]
                        if estimate_i > estimate: estimate = estimate_i
                    estimate = d + estimate
                    heappush(queue, (estimate, d, w, v))
    return distance, landmark_path(parents, source, destination) if distance < float("inf") else []

def best_landmarks(source, destination, landmarks, n_landmark):
    # source: coordinates of source
    # destination: coordinates of destination
    # landmarks: list of nodes that are landmarks
    # return: a list of 4 indexes of the landmarks to use from 'nodes'
    #         where nodes is the list of tuples passed to landmark()
    #         (longitude, latitude, dist(1,1), dist(1,2),..., dist(n_landmark,1), dist(n_landmark,2))
    # find 'best': the 2 landmarks closest to source + the 2 landmarks closest to destination
    distances_sources = sorted([(_distance(source, landmarks[i]), i) for i in xrange(n_landmark)])
    distances_destination = sorted([(_distance(destination, landmarks[i]), i) for i in xrange(n_landmark)])
    best = set([distances_sources[0][1], distances_sources[1][1], distances_destination[0][1], distances_destination[1][1]])
    if len(best) == 2:
        # find 2 other landmarks
        # because len(best) == 2, distances_sources[:2] == distances_destination[:2]
        # we'll take the closest from distances_sources[2:4] + distances_destination[2:4]
        new_best = sorted(distances_sources[2:4] + distances_destination[2:4])
        best.add(new_best[0][1])
        if new_best[1][1] == new_best[0][1]:
            best.add(new_best[2][1])
        else:
            best.add(new_best[1][1])
    elif len(best) == 3:
        # find 1 other landmark
        # either distances_sources[2][1] or distances_destination[2][1] is not in best
        if distances_sources[2][1] in best:
            best.add(distances_destination[2][1])
        else:
            best.add(distances_sources[2][1])
    return best
    
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
