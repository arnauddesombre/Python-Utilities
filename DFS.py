"""
explore a graph using Depth First Search (DFS)

return a dictionary containing the visiting order
for each node starting at visited[source] = 1
"""
import sys
sys.setrecursionlimit(1000000)

def DFS(graph, source, count=0, visited={}):
    count += 1
    if source not in visited:
        visited[source] = 0
    visited[source] = count
    for node in graph[source]:
        if node not in visited:
            visited[node] = 0
        if visited[node] == 0:
            DFS(graph, node, count, visited)
    return visited


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
