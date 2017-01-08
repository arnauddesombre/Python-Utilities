"""
Kruskal's MST (minimum spanning tree) algorithm

costs can be negative.
MST assumes the graph is undirected.

'graph' is defined as: graph = {from:{to:dist, ...}, ...}
if graph[from][to] == dist, it is assumed that graph[to][from] == dist as well
therefore in the MST, the edge would be [from, to, dist] or [to, from, dist]

/!\ if both graph[from][to] and graph[to][from] are defined, even with the same
value, it would be assumed that this creates 2 different edges between 'from' and 'to'
(which would have no impact on the output)
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

def kruskal(nodes, graph):
    """
    input:   graph   = in dictionary form {from:{to:distance, ...}, ...}
             nodes   = list of all nodes
    output:  the MST = list of (head, tail, weight)
    """
    init()
    mst = []
    edges = set()
    for u in graph:
        for v in graph[u]:
            if u < v:
                edges.add((graph[u][v], u, v))
            else:
                edges.add((graph[u][v], v, u))
    edges = list(edges)
    edges = sorted(edges, key=lambda x:x[0])
    count = 0
    total = len(nodes) - 1
    for node in nodes:
        make_set(node)
    for length, u, v in edges:
        if union(u, v):
            mst.append((u, v, length))
            count += 1
            if count == total:
                break
    return mst


############################
#        E
#       / \
#     1/   \-1
#     D--3--C
#     |     |
#     2     3
#     |     |
#     A--1--B
#

if __name__ == "__main__":
    
    nodes = set(['A', 'B', 'C', 'D', 'E'])
    graph = {'A': {'B':1, 'D':2},
             'B': {'C':3},
             'C': {'D':3, 'E':-1},
             'D': {'E':1},
             'E': {}}

    print
    print kruskal(nodes, graph)
    print
