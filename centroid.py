'''
Centroid Decomposition of a Tree

For more information, see:
https://threads-iiith.quora.com/Centroid-Decomposition-of-a-Tree
'''

import sys
sys.setrecursionlimit(200000)

def initialize_level(graph, root):
    # return:
    # the level of each node from root (level[node] = distance from root)
    # the height of the tree (largest distance from root)
    # the parent dictionary (parent[root] = None)
    dist = 0
    queue = [(root, dist)]
    visited = set()
    level = {}
    H = 0
    parent = {root:None}
    while queue:
        node, dist = queue.pop(0)
        visited.add(node)
        level[node] = dist
        if node in graph:
            dist += 1
            for children in graph[node]:
                if children not in visited:
                    queue.append((children, dist))
                    parent[children] = node
                    H = dist
    return level, H, parent

def count_nodes(graph, start, exclude1, exclude2 = set()):
    # return the number of nodes in the tree defined by 'graph'
    # starting at node 'start' and excluding nodes in 'exclude1' and 'exclude2'
    if start in exclude1 or start in exclude2:
        return 0
    queue = [start]
    visited = set()
    count = 0
    while queue:
        node = queue.pop(0)
        visited.add(node)
        count += 1
        if node in graph:
            for child in graph[node]:
                if child not in visited and child not in exclude1 and child not in exclude2:
                    queue.append(child)
    return count

def find_centroid(graph, n, start, exclude = set()):
    # return the centroid of the tree defined by 'graph'
    # starting at node 'start' and excluding nodes in 'exclude'
    # /!\ this function is recursive
    node_max = None
    if start in graph:
        for node in graph[start]:
            if node not in exclude:
                size = count_nodes(graph, node, exclude, {start})
                if size > n / 2:
                    node_max = node
                    break
    if node_max != None:
        return find_centroid(graph, n, node_max, exclude)
    else:
        return start

def build_centroid_recursively(graph, n, tree = {}, center = None, exclude = set()):
    # build the centroid tree as the dictionary 'tree' (global variable)
    # tree['root'] = the root of tree
    # tree[u] = set of all nodes connected to node u
    if center == None:
        center = find_centroid(graph, n, list(graph.keys())[0])
        tree = {'root':center}
    if center not in tree:
        tree[center] = set()
    if center in graph:
        exclude.add(center)
        for child in graph[center]:
            if child not in exclude:
                n2 = count_nodes(graph, child, exclude)
                center2 = find_centroid(graph, n2, child, exclude)
                tree[center].add(center2)
                build_centroid_recursively(graph, n2, tree, center2, exclude)
    return tree

def build_parent_centroid(tree):
    # return a dictionary containing the parent node for
    # all nodes in the centroid tree
    parent = {}
    if 'root' not in tree:
        return parent, level
    queue = [(tree['root'])]
    parent[tree['root']] = None
    while queue:
        node = queue.pop(0)
        if node in graph:
            for child in tree[node]:
                queue.append((child))
                parent[child] = node
    return parent

def build_centroid(graph, n):
    # build the centroid associated with 'graph'
    # return:
    # centroid_root = the root of the centroid tree
    #      1 <= centroid_root <= n
    # centroid_tree = the centroid tree
    #      centroid_tree[u] = [v1, v2, ...]
    # centroid_level = the level in the centroid tree
    #      centroid_level[centroid_root] = 0
    # centroid_height = the height of the original tree
    #      is about math.log(n, 2)
    # centroid_parent_graph = the parent dictionary in the centroid tree
    #      centroid_parent_graph[centroid_root] = None
    centroid_tree = build_centroid_recursively(graph, n)
    parent_centroid = build_parent_centroid(centroid_tree)
    centroid_root = centroid_tree['root']
    centroid_level, centroid_height, centroid_parent_graph = initialize_level(centroid_tree, centroid_root)
    del centroid_tree['root']
    return centroid_root, centroid_tree, centroid_level, centroid_height, centroid_parent_graph

if __name__ == '__main__':
    '''
    Below is the solution for the problem:
    C. Ciel the Commander
    http://codeforces.com/problemset/problem/321/C
    (Time limit exceeded on test 12, however CodeForces give the same time for Python and C++)
    '''
    # Read input
    # n : number of nodes
    try:
        n = int(raw_input().strip())
    except:
        n = int(input().strip())
    # nodes : list of all nodes, numbered from 1 to n
    nodes = range(1, n + 1)
    # graph : dictionary where keys are the nodes
    # graph[u] : set of nodes connected to u = (v, ...)
    # graph is bi-directional
    graph = {}
    parent_graph = {}
    for node in nodes:
        graph[node] = set()
    for edge in range(n - 1):
        try:
            u, v = map(int, raw_input().strip().split())
        except:
            u, v = map(int, input().strip().split())
        graph[u].add(v)
        graph[v].add(u)

    root, tree, level, height, parent = build_centroid(graph, n)
    if height > 26:
        print("Impossible!")
    else:
        output = [chr(ord('A') + level[i]) for i in nodes]
        print(' '.join(output))
        
