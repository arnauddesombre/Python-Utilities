'''
Implementation of Lowest Common Ancestor algorithms
see:
https://www.hackerrank.com/topics/lowest-common-ancestor

For demo, run:
@call C:\Software\Python27\_arnaud\anaconda27.bat
python lca.py < lca.txt
'''

import sys
sys.setrecursionlimit(100000)   # for Naive #1, sqrt(N)
from math import sqrt           # for sqrt(N)
from math import log            # for log(N)


# Naive algorithm #1: no parent dictionary
#  - No pre-processing
#  - Time complexity per query: O(N)

def path_from_root(graph, root, node):
    # return the path from root to node in graph
    # return [] if no path exists
    if root not in graph:
        return []
    if root == node:
        return [node]
    for children in graph[root]:
        if children == node:
            return [root, node]
        path = path_from_root(graph, children, node)
        if path != []:
            return [root] + path
    return []

def lca_N_1(graph, root, u, v):
    # return the least common ancestor of u and v
    path_u = path_from_root(graph, root, u)
    path_v = path_from_root(graph, root, v)
    if path_u == [] or path_v == []:
        return None
    if path_u[0] != root or path_v[0] != root:
        return None
    ancestor = root
    for i in range(min(len(path_u), len(path_v))):
        if path_u[i] != path_v[i]:
            break
        ancestor = path_u[i]
    return ancestor


# Naive algorithm #2: with parent dictionary
#  - No pre-processing
#  - Time complexity per query: O(N)

def lca_N_2(parent, u, v):
    # root is the node where parent[root] == None
    if u not in parent or v not in parent:
        return None
    path_u = set([u])
    node = parent[u]
    while node != None:
        path_u.add(node)
        node = parent[node]
    node = v
    while node not in path_u and node != None:
        node = parent[node]
    return node


# LCA using square-root decomposition
#  - Time complexity for pre-processing: O(N)
#  - Time complexity per query: O(sqrt(N))

def initialize_level(graph, root):
    # return the level of each node from root
    # level[node] = distance from root
    # /!\ graph is a Directed Acyclic Graph, there is
    #     no need to maintain a visited set
    dist = 0
    queue = [(root, dist)]
    level = {}
    H = 0
    while queue:
        node, dist = queue.pop(0)
        level[node] = dist
        if node in graph:
            dist += 1
            if graph[node] != []:
                H = dist
                for children in graph[node]:
                    queue.append((children, dist))
    return level, H

def pre_computation_sqrt_n(graph, level, H, node, head, prev_section, P):
    current_section = int(level[node] / sqrt(H)) + 1
    if current_section == 1:
        P[node] = 1
    else:
        if current_section == prev_section + 1:
            P[node] = parent[node]
            head = node
        else:
            P[node] = parent[head]
    if node in graph:
        for child in graph[node]:
            if level[child] > level[node]:
                pre_computation_sqrt_n(graph, level, H, child, head, current_section, P)

def lca_sqrt_n(level, parent, P, u, v):
    if u not in P or v not in P:
        return None
    while P[u] != P[v]:
        if level[u] > level[v]:
            u = P[u]
        else:
            v = P[v]
    while u != v:
        if level[u] > level[v]:
            u = parent[u]
        else:
            v = parent[v]
    return u


# LCA using sparse table
#  - Time complexity for pre-processing: O(N*Log(N))
#  - Time complexity per query: O(Log(N))

'''
# need function defined in the sqrt(n) section
def initialize_level(graph, root):
'''

def pre_computation_log_n(parent, n, log_n):
    P = [[-1] * (log_n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        P[i][0] = parent[i]
    for j in range(1, log_n + 1):
        for i in range(1, n + 1):
            if P[i][j-1] != -1:
                P[i][j] = P[P[i][j-1]][j-1]
    return P

def lca_log_n(log_n, level, P, u, v):
    if u not in level or v not in level:
        return None
    if level[u] < level[v]:
        u, v = v, u
    dist = level[u] - level[v]
    while dist > 0:
        raise_by = int(log(dist, 2))
        u = P[u][raise_by]
        dist -= 2 ** raise_by
    if u == v:
        return u
    for j in range(log_n, -1, -1):
        if P[u][j] != -1 and P[u][j] != P[v][j]:
            u = P[u][j]
            v = P[v][j]
    return parent[u]


if __name__ == '__main__':
    # Read input
    # n : number of nodes
    # m : number of edges (= m - 1)
    try:
        n, m = map(int, raw_input().strip().split())
    except:
        n, m = map(int, input().strip().split())
    # nodes : list of all nodes, numbered from 1 to n
    nodes = range(1, n + 1)
    root = 1
    # graph : dictionary where keys are the nodes
    # graph[u] : list of nodes connected to u = [v, ...]
    # parent : dictionary of ancestor
    # graph[u] = v  =>  parent[v] = u
    graph = {}
    for node in range(n):
        graph[node] = []
    parent = {root:None}
    for edge in range(m):
        try:
            u, v = map(int, raw_input().strip().split())
        except:
            u, v = map(int, input().strip().split())
        graph[u].append(v)
        parent[v] = u
    print('PATH')
    print(path_from_root(graph, root, 2))
    print(path_from_root(graph, root, 8))
    print(path_from_root(graph, root, 13))
    print(path_from_root(graph, root, 99))
    print
    print('ANCESTOR')
    print('O(N)')
    print(lca_N_1(graph, root, 5, 10), lca_N_2(parent, 5, 10))
    print(lca_N_1(graph, root, 5, 9), lca_N_2(parent, 5, 9))
    print(lca_N_1(graph, root, 12, 11), lca_N_2(parent, 12, 11))
    print(lca_N_1(graph, root, 5, 99), lca_N_2(parent, 5, 99))
    print('O(sqrt(N))')
    P = {}
    level, H = initialize_level(graph, root)
    pre_computation_sqrt_n(graph, level, H, root, root, 1, P)
    print(lca_sqrt_n(level, parent, P, 5, 10))
    print(lca_sqrt_n(level, parent, P, 5, 9))
    print(lca_sqrt_n(level, parent, P, 12, 11))
    print(lca_sqrt_n(level, parent, P, 5, 99))
    print('O(log(N))')
    parent[root] = root # not None
    level, H = initialize_level(graph, root)
    log_n = int(log(n, 2))
    P = pre_computation_log_n(parent, n, log_n)
    print(lca_log_n(log_n, level, P, 5, 10))
    print(lca_log_n(log_n, level, P, 5, 9))
    print(lca_log_n(log_n, level, P, 12, 11))
    print(lca_log_n(log_n, level, P, 5, 99))


