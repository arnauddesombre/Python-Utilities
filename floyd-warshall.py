"""
Floyd-Warshall algorithm
all-pairs shortest paths
"""

def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    for u in graph:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = graph[u][v]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


############################
#  0: connected to cycle 1-2-3
#     and connected to other cycle 4-5-6

if __name__ == "__main__":
    
    graph = {0:{1:1, 4:1},
             1:{2:1},
             2:{3:-1},  # negative cycle: -1=no, -10=yes
             3:{1:1},
             4:{5:1},
             5:{6:-1},  # negative cycle: -1=no, -10=yes
             6:{4:1}}
    
    n = len(graph)
    matrix = floyd_warshall(graph, n)

    for k in range(n):
        if matrix[k][k] < 0:
            print("Graph contains a negative-weight cycle")
            print()
            break

    from pprint import pprint
    pprint(matrix)
