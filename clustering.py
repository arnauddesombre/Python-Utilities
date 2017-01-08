"""
returns k clusters from an undirected graph, using
Kruskal's MST (minimum spanning tree) algorithm

costs can be negative
'graph' is defined as: graph = {from:{to:dist, ...}, ...}
if graph[from][to] == dist, it is assumed that graph[to][from] == dist as well
therefore in the MST, the edge would be [from, to, dist] or [to, from, dist]

/!\ if both graph[from][to] and graph[to][from] are defined, even with the same
value, it would be assumed that this creates 2 different edges between 'from' and 'to'
(which would have no impact on the output)

Return:
a dictionary of integer keys 1 to k containing the list of nodes of each cluster
the minimum distance between the k clusters
"""

def init():
    global parent, rank
    parent = {}
    rank = {}

def make_set(node):
    global parent, rank
    parent[node] = node
    rank[node] = 0

def find(node):
    if parent[node] == node:
        return node
    else:
        return find(parent[node])

def union(node1, node2):
    global parent, rank
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        # Attach smaller rank tree under root of higher rank tree
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1] = root2
        else:
            # If ranks are same, make one as root and increment its rank by one
            parent[root1] = root2
            rank[root2] += 1
        return True
    else:
        return False

from random import randint

def clustering(nodes, graph, k):
    """
    input:   graph   = in dictionary form {from:{to:distance, ...}, ...}
             nodes   = list of all nodes
             k       = number of clusters
    output:  a dictionary of keys 1 to k containing the list of nodes of each cluster
             the minimum distance between the k clusters
    """
    # Kruskal (adapted)
    init()
    edges = set()
    for u in graph:
        for v in graph[u]:
            if u < v:
                edges.add((graph[u][v], u, v))
            else:
                edges.add((graph[u][v], v, u))
    edges = list(edges)
    edges = sorted(edges, key=lambda x:x[0])
    count = len(nodes)
    dist = float("inf")
    for node in nodes:
        make_set(node)
    for length, u, v in edges:
        if count == k:
            dist = length
            break
        if union(u, v):
            count -= 1
    # computes clusters
    cluster = {}
    for node in nodes:
        root = find(node)
        if root not in cluster:
            cluster[root] = []
        cluster[root].append(node)
    # change cluster keys
    # first, make sure no keys are already integer between 1 and k
    for key in cluster:
        if key in xrange(k+1):
            seed = str(key)
            while seed in cluster:
                seed = seed + str(randint(0,9))
            cluster[str(key)] = cluster.pop(key)
    # then change key to 1...k
    count = 1
    for key in cluster:
        cluster[count] = cluster.pop(key)
        count += 1
    return cluster, dist


############################
#        E
#       / \
#     4/   \-1
#     D--3--C
#     |     |
#     2     3
#     |     |
#     A--1--B
#

if __name__ == "__main__":
    
    nodes = set(['A', 'B', 'C', 'D', 'E'])
    graph = {'A': {'B':1,  'D':2},
             'B': {'A':1,  'C':3},
             'C': {'B':3,  'D':3, 'E':-1},
             'D': {'A':2,  'C':3, 'E':4},
             'E': {'C':-1, 'D':4}}

    k = 3
    cluster = clustering(nodes, graph, k)
    print "clusters:"
    for x in xrange(1, k+1):
        print x, "=", cluster[0][x]
    print "minimum distance =", cluster[1]
    print
