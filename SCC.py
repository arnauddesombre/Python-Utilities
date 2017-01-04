"""
Strongly Connected Components

Compute the SCC of a directed graph using the Kosaraju's algorithm

return:
- the number of SCC
- a dictionary SCC1, SCC1[n] = list of all nodes in SCC number 'n'
- a dictionary SCC2, SCC2[node] = number of the SCC of which 'node' is a member
"""

# recursion will crash for large graphs
recursive = False

import sys
sys.setrecursionlimit(500000)

def init():
    global clock, pre, post, pre_node, post_node, revgraph
    clock = 0
    pre = {}
    post = {}
    pre_node = {}
    post_node = {}
    revgraph = {}

def previsit(node):
    global clock, pre, pre_node
    pre[node] = True   # any value (not necessary for Kosaraju)

def postvisit(node):
    global clock, post, post_node
    clock += 1
    post[node] = clock
    post_node[clock] = node

def explore(source):
    if recursive:
        explore_recursive(source)
    else:
        explore_linear(source)

def explore_recursive(source):
    # recursive DFS
    previsit(source)
    for node in revgraph[source]:
        if node not in pre:
            explore(node)
    postvisit(source)

def explore_linear(source):
    # linear DFS
    for node in revgraph:
        if node in post:
            continue
        previsit(node)
        stack = [(node, revgraph[node].__iter__())]
        while stack:
            x, iterator = stack.pop()
            try:
                y = next(iterator)
                stack.append((x, iterator))
                if y in pre or y in post:
                    continue
                previsit(y)
                stack.append((y, revgraph[y].__iter__()))
            except StopIteration:
                postvisit(x)

def reverse(nodes, graph):
    rev = {}
    for node in nodes:
        rev[node] = {}
    for node1 in graph:
        for node2 in graph[node1]:
            rev[node2][node1] = graph[node1][node2]
    return rev

def BFS(graph, source, largest_post):
    # return list of nodes discoverable from source
    queue = [source]
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        for adjacent in graph[node]:
            if post[adjacent] < largest_post:
                if adjacent not in visited:
                    queue.append(adjacent)
    return list(visited)

def SCC(nodes, graph):
    """
    Algorithm for SCCs(G):
    Run DFS on reverse graph (revgraph)
    for v in V in reverse postorder:
        if not visited(v):
            Explore(v)
            mark visited vertices as new SCC
    """
    global revgraph
    init()

    # DFS on reverse of graph
    revgraph = reverse(nodes, graph)
    source = graph.keys()[0]
    missing = True
    while missing:
        explore(source)
        missing = False
        for node in nodes:
            if node not in post:
                missing = True
                source = node
                break

    # explore graph starting with the largest post number value
    scc = 0   # number of SCC
    SCC1 = {} # SCC1[n] = list of all nodes in SCC number 'n'
    SCC2 = {} # SCC2[node] = number of the SCC of which 'node' is a member
    largest_post = clock
    while True:
        # find largest post value not already in a SCC
        while largest_post > 0:
            largest_node = post_node[largest_post]
            if largest_node not in SCC2:
                break
            else:
                largest_post -= 1
        if largest_post == 0:
            break
        # explore from largest_node
        scc += 1
        SCC1[scc] = BFS(graph, largest_node, largest_post)
        for node in SCC1[scc]:
            SCC2[node] = scc
        largest_post -= 1
    
    return scc, SCC1, SCC2


############################

if __name__ == "__main__":

    nodes = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ,'I'])
    graph = {'A': {'B':1},
             'B': {'E':1, 'F':1},
             'C': {'B':1},
             'D': {'A':1, 'G':1},
             'E': {'A':1, 'C':1, 'H':1},
             'F': {},
             'G': {'H':1},
             'H': {'I':1},
             'I': {'H':1, 'F':1}}

    scc, SCC1, SCC2 = SCC(nodes, graph)
    print scc, "components"
    print SCC1
    print SCC2
