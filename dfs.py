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
    previsit(source)
    stack = [(source, graph[source].__iter__())]
    while stack:
        x, iterator = stack.pop()
        try:
            y = next(iterator)
            stack.append((x, iterator))
            if y not in pre_visit:
                previsit(y)
                stack.append((y, graph[y].__iter__()))
        except StopIteration:
            postvisit(x)
    return pre_visit, post_visit

############################
#       1   2   3
#        \ / \ /
#    12---A---B----4
#        / \ / \
#  11---F---X---C---5
#        \ / \ /
#    10---E---D---6
#        / \ / \
#       9   8   7---F1---F2
#
# all distances are equal to 1

if __name__ == "__main__":
    
    nodes = set(['X', 'A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', "F1", "F2"])
    graph = {'X':  {'A':1, 'B':1, 'C':1,  'D':1, 'E':1,  'F':1},
             'A':  {'1':1, '2':1, 'B':1,  'X':1, 'F':1, '12':1},
             'B':  {'2':1, '3':1, '4':1,  'C':1, 'X':1,  'A':1},
             'C':  {'B':1, '5':1, 'D':1,  'X':1},
             'D':  {'X':1, 'C':1, '6':1,  '7':1, '8':1,  'E':1},
             'E':  {'F':1, 'X':1, 'D':1,  '8':1, '9':1, '10':1},
             'F':  {'A':1, 'X':1, 'E':1, '11':1},
             '1':  {'A':1},
             '2':  {'A':1, 'B':1},
             '3':  {'B':1},
             '4':  {'B':1},
             '5':  {'C':1},
             '6':  {'D':1},
             '7':  {'D':1, 'F1':1},
             '8':  {'D':1, 'E':1},
             '9':  {'E':1},
             '10': {'E':1},
             '11': {'F':1},
             '12': {'A':1},
             'F1': {'7':1, 'F2':1},
             'F2': {'F2':1}}

    x1 = DFS(graph, 'X')
    x2 = DFS_recursive(graph, 'X')
    x3 = DFS_linear(graph, 'X')
    print x1[0]
    print x2[0]
    print x3[0]
    print
    print x1[1]
    print x2[1]
    print x3[1]

