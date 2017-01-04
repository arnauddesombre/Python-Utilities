"""
explore a graph using Depth First Search (DFS)

compute dictionaries containing the visiting orders
(pre_visit & post_visit) for each node starting at 1

implements:
DFS_recursive(graph, source): a recursive algorithm
DFS_linear(graph, source): a linear algorithm
DFS(graph, source, rec=False): which calls one or the other (default: 'rec')
"""

# recursion will eventually crash for large graphs
recursive = False

import sys
sys.setrecursionlimit(1000000)

def init():
    global pre_clock, post_clock, pre_visit, post_visit
    pre_clock = 0
    post_clock = 0
    pre_visit = {}
    post_visit = {}

def previsit(node):
    global pre_clock, pre_visit
    pre_clock += 1
    pre_visit[node] = pre_clock

def postvisit(node):
    global post_clock, post_visit
    post_clock += 1
    post_visit[node] = post_clock

def DFS(graph, source, rec=recursive):
    if rec:
        return DFS_recursive(graph, source)
    else:
        return DFS_linear(graph, source)

def DFS_recursive(graph, source, first_time=True):
    # recursive DFS
    if first_time:
        init()
    previsit(source)
    for node in graph[source]:
        if node not in pre_visit:
            DFS_recursive(graph, node, False)
    postvisit(source)
    if first_time:
        return pre_visit, post_visit
    else:
        return

def DFS_linear(graph, source):
    # linear DFS
    init()
    for node in graph:
        if node in post_visit:
            continue
        previsit(node)
        stack = [(node, graph[node].__iter__())]
        while stack:
            x, iterator = stack.pop()
            try:
                y = next(iterator)
                stack.append((x, iterator))
                if y in pre_visit or y in post_visit:
                    continue
                previsit(y)
                stack.append((y, graph[y].__iter__()))
            except StopIteration:
                postvisit(x)
    return pre_visit, post_visit


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
             'E': {'C':2, 'D':1}}

    print DFS(graph, 'A')
    print DFS_recursive(graph, 'A')
    print DFS_linear(graph, 'A')
