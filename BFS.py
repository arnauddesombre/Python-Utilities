"""
explore a graph using Breadth First Search (BFS)

return a dictionary containing the visiting order
for each node starting at visited[source] = 1
"""

def BFS(graph, source):
    count = 0
    queue = [source]
    visited = {source:count}
    while queue:
        count += 1
        node = queue.pop(0)
        visited[node] = count
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited[adjacent] = 0
                queue.append(adjacent)
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

    print BFS(graph, 'A')
