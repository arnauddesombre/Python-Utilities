"""
Bellman-Ford algorithm

bellman_ford(graph, source) compute all shortest distances from 'source'
to all points in 'graph' as well as the shortest corresponding paths.
'graph' is a directed graph.
/!\ distances can be < 0
/!\ no negative cycle

return:
dist = shortest distances
dist[node] is the shortest distance from source to node
parent = shortest path parents dictionary
parent[node] is the parent of node in the shortest path from the given source
cycle = True if there is a negative cycle, False otherwise

if 'cycle' == True, negative_cycle(graph, source) will return a list containing
one negative cycle (note there can be multiple negative cycles). The first
and last element of the list are the same ([A, B, ... , A])

if not, bellman_ford_path(parents, source, destination) will return the
path (a list) from 'source' to 'destination'. Note that if there is a negative
loop, this function will run indefinitely
"""

def relax(u, v, graph, dist, parent):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]
        parent[v] = u
        return True
    else:
        return False

def bellman_ford(graph, source):
    dist = {}
    parent = {}
    for node in graph:
        dist[node] = float('Inf')
        parent[node] = None
    dist[source] = 0
    last_relaxed_node = None
    for _ in xrange(len(graph) - 1):
        has_relaxed = False
        for u in graph:
            for v in graph[u]:
                if relax(u, v, graph, dist, parent):
                    has_relaxed = True
                    last_relaxed_node = v
        if not has_relaxed:
            break
    # test for negative cycle
    cycle = False
    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                cycle = True
                break
    return dist, parent, cycle, last_relaxed_node if cycle else None

def bellman_ford_path(parents, source, destination):
    node = destination
    path = [node]
    while node != source:
        if node in parents:
            node = parents[node]
            path.append(node)
        else:
            return []
    return path[::-1]   

def negative_cycle(graph, source):
    # return 1 negative cycle in 'graph'
    node = None
    for _ in xrange(len(graph) - 1):
        dist, parent, cycle, node = bellman_ford(graph, source)
        if not cycle:
            return []
    # 'node' is reachable from a negative cycle
    for _ in xrange(len(graph) - 1):
        node = parent[node]
    # 'node' is on a negative cycle
    path = [node]
    new_node = node
    while True:
        new_node = parent[new_node]
        path.append(new_node)
        if new_node == node:
            break
    return path[::-1]


############################
#        E
#       / \
#     1/   \-2.5 for E->C and +3 for C->E
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
             'C': {'B':3, 'D':3, 'E':3},
             'D': {'A':2, 'C':3, 'E':1},  # use 'E':-0.6 for C-D-E-C negative cycle
             'E': {'C':-2.5, 'D':1}}

    BF = bellman_ford(graph, 'A')
    if BF[2]:
        print "There is a negative cycle"
        print "Bellman-Ford failed"
        print "One negative cycle is:"
        print negative_cycle(graph, 'A')
    else:
        print "There is no negative cycle"
        print "Bellman-Ford is correct"
        print
        print "Parent dictionary:"
        print BF[0]
        print
        print "Path from 'A' to 'C'"
        print bellman_ford_path(BF[1], 'A', 'C')
