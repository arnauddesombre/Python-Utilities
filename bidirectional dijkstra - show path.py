"""
compute the shortest distance from a source to a destination
in a directed graph as well as the shortest corresponding path
using bi-directional Dijkstra algorithm
/!\ all distances must be >= 0

return:
shortest distance
shortest path from 'source' to 'destination'
"""
from heapq import heappush, heappop

def reverse(nodes, graph):
    rev = {}
    for node in nodes:
        rev[node] = {}
    for node1 in graph:
        for node2 in graph[node1]:
            rev[node2][node1] = graph[node1][node2]
    return rev

def bi_dijkstra(nodes, graph, source, destination, graph_rev=None):
    if graph_rev == None:
        graph_rev = reverse(nodes, graph)

    dist, dist_rev = {}, {}
    parents, parents_rev = {}, {}
    queue, queue_rev = [(0, source, None)], [(0, destination, None)]
    visited_nodes, visited_nodes_rev = {}, {}
    while queue or queue_rev:
        # process queue
        if queue:
            path_len, v, parent = heappop(queue)
            if v not in visited_nodes:
                visited_nodes[v] = True
                dist[v] = path_len
                parents[v] = parent
                if v in visited_nodes_rev:
                    break
                for w, edge_len in graph[v].items():
                    if w not in visited_nodes:
                        if (w in dist and path_len + edge_len < dist[w]) or (w not in dist):
                            dist[w] = path_len + edge_len
                            parents[w] = v
                            heappush(queue, (dist[w], w, v))
        # process queue_rev
        if queue_rev:
            path_len, v, parent = heappop(queue_rev)
            if v not in visited_nodes_rev:
                visited_nodes_rev[v] = True
                dist_rev[v] = path_len
                parents_rev[v] = parent
                if v in visited_nodes:
                    break
                for w, edge_len in graph_rev[v].items():
                    if w not in visited_nodes_rev:
                        if (w in dist_rev and path_len + edge_len < dist_rev[w]) or (w not in dist_rev):
                            dist_rev[w] = path_len + edge_len
                            parents_rev[w] = v
                            heappush(queue_rev, (dist_rev[w], w, v))

    # process shortest path and shortest distance
    distance = float("inf")
    u_best = None
    for node in list(visited_nodes.keys()) + list(visited_nodes_rev.keys()):
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
#     1/   \2
#     D--3--C
#     |     |
#     2     3
#     |     |
#     A--1--B
#

if __name__ == "__main__":
    
    nodes = set(['A', 'B', 'C', 'D', 'E'])
    graph = {'A': {'B':1, 'D':2},
             'B': {'A':1, 'C':3},
             'C': {'B':3, 'D':3, 'E':2},
             'D': {'A':2, 'C':3, 'E':1},
             'E': {'C':1, 'D':1}}

    source = 'A'
    destination = 'C'
    dist, path = bi_dijkstra(nodes, graph, source, destination)

    print(dist)
    print(path)
    print
