"""
Bellman-Ford algorithm

bellman_ford(graph, source) compute all shortest distances from 'source'
to all points in 'graph' as well as the shortest corresponding paths.
'graph' is a directed graph.
/!\ distances can be < 0
/!\ no negative cycle

return:
dist = shortest distances
dist[node] is the shortest distance from 'source' to 'node'
parent = shortest path parents dictionary
cycle = set of nodes in negative cycle(s) (empty if none)
"""

def bellman_ford(graph, source):
    dist = {}
    parent = {}
    for node in graph:
        dist[node] = float('Inf')
        parent[node] = None
    dist[source] = 0
    for _ in range(len(graph) - 1):
        relaxed = False
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u
                    has_relaxed = True
        if not relaxed:
            break
    # test for negative cycles
    cycle = set()
    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                cycle.add(u)
                cycle.add(v)
    return dist, parent, cycle


############################
#  0: connected to cycle 1-2-3-4-5
#     and connected to other cycle 10-11-12-13-14-15

if __name__ == "__main__":
    
    graph = {0:{1:1, 10:1},
             1:{2:1},
             2:{3:-10},  # negative cycle: -1=no, -10=yes
             3:{4:1},
             4:{5:1},
             5:{1:1},
             10:{11:1},
             11:{12:-10},  # negative cycle: -1=no, -10=yes
             12:{13:1},
             13:{14:1},
             14:{15:1},
             15:{10:1}}
    
    BF = bellman_ford(graph, 0)
    if BF[2]:
        print("There is at least 1 negative cycle")
        print("Bellman-Ford failed")
        print()
        print("some nodes on all negative cycle(s)")
        print(BF[2])
        print()
    else:
        print("There is no negative cycle")
        print("Bellman-Ford is correct")
        print()
        print("distances from source:")
        print(BF[0])
        print()
    print("Parent dictionary:")
    print(BF[1])
