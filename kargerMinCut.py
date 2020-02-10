"""
see proof of correctness:
https://www.hackerrank.com/contests/w37/challenges/two-efficient-teams/submissions/code/13073776001
"""

import random
import math
import copy

class Graph():
    """
    an undirected graph is represented by:
    nodes  = set of nodes
    edges  = dictionary of edges,
             edges[(n1, n2)] = value means that the edge
             between n1 and n2 has the (integer) value
    n / m  = total number of nodes / edges
    groups = determine the 2 groups for the cut
    """

    def __init__(self):
        self.nodes = set()
        self.n = 0
        self.edges = {}
        self.m = 0
        self.groups = {}

    def size(self):
        return self.n

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.n += 1
            self.groups[node] = self.n

    def addEdge(self, node1, node2, value):
        assert node1 in self.nodes
        assert node2 in self.nodes
        assert node1 != node2
        assert value > 0
        if (node1, node2) in self.edges:
            self.edges[(node1, node2)] += value
        elif (node2, node1) in self.edges:
            self.edges[(node2, node1)] += value
        else:
            self.edges[(node1, node2)] = value
        self.m += value

    def randomEdge(self):
        # return an edge (node1, node2) chosen randomly among all edges
        # note: randomly picking a node, and randomly picking an edge
        #       from that node is obviously not the same thing (and is wrong)
        rnd = random.randint(0, self.m - 1)
        cumul = 0
        for edge in self.edges:
            if self.edges[edge] > 0:
                if cumul <= rnd < cumul + self.edges[edge]:
                    return edge
                cumul += self.edges[edge]

    def contractEdge(self, node1, node2):
        # contract edge (node1, node2): node2 is contracted onto node1
        assert node1 != node2
        assert (node1, node2) in self.edges
        assert self.edges[(node1, node2)] > 0 
        # replace all edges (w, node2) and (node2, w) with (w, node1)
        for w in self.nodes:
            if (w, node2) in self.edges:
                if (w, node1) not in self.edges:
                    self.edges[(w, node1)] = 0
                self.edges[(w, node1)] += self.edges[(w, node2)]
                self.edges[(w, node2)] = 0
            if (node2, w) in self.edges:
                if (w, node1) not in self.edges:
                    self.edges[(w, node1)] = 0
                self.edges[(w, node1)] += self.edges[(node2, w)]
                self.edges[(node2, w)] = 0
        # remove self-loop (node1, node1) and (node2, node2)
        if (node1, node1) in self.edges:
            self.m -= self.edges[(node1, node1)]
            self.edges[(node1, node1)] = 0
        if (node2, node2) in self.edges:
            self.m -= self.edges[(node2, node2)]
            self.edges[(node2, node2)] = 0
        # update groups
        g1 = self.groups[node1]
        g2 = self.groups[node2]
        for node in self.groups:
            if self.groups[node] == g2:
                self.groups[node] = g1
        # remove node2
        self.nodes.remove(node2)
        self.n -= 1

    def kargerMinCut(self):
        assert self.n >= 2
        assert self.m >= 1
        while self.n > 2:
            node1, node2 = self.randomEdge()
            self.contractEdge(node1, node2)
        # only 2 nodes remain in self.nodes
        (node1, node2) = self.nodes
        group1 = [node for node in self.groups if self.groups[node] == self.groups[node1]]
        group2 = [node for node in self.groups if self.groups[node] == self.groups[node2]]
        nCut = 0
        if (node1, node2) in self.edges:
            nCut += self.edges[(node1, node2)]
        if (node2, node1) in self.edges:
            nCut += self.edges[(node2, node1)]
        return nCut, group1, group2

    def BFS(self):
        # perform a BFS from a random node
        # return group1, group2 where:
        # group1 is the group of nodes connected to the initial random node
        # group2 is the group of other nodes
        # if group2 != [], there is a trivial cut for the graph
        assert self.n >= 1
        for source in self.nodes:
            break
        # 'source' is an element of self.nodes
        queue = [source]
        visited = set()
        while queue:
            node = queue.pop(0)
            visited.add(node)
            for (node1, node2) in self.edges:
                if self.edges[(node1, node2)] > 0:
                    if node1 == node:
                        if node2 not in visited:
                            queue.append(node2)
                    if node2 == node:
                        if node1 not in visited:
                            queue.append(node1)
        group1 = list(visited)
        group2 = [node for node in self.nodes if node not in visited]
        return group1, group2

def kargerMinCut(graph):
    """
    return the minimum number of cuts
    of n * n * log(n) cuts of graph
    """
    # check if there is a trivial solution (when the graph is not connected!)
    group1, group2 = graph.BFS()
    if group2:
        return 0, group1, group2
    minCut = float('inf')
    group1 = []
    group2 = []
    n = graph.size()
    iteration = int(n * n * math.log(n, 2))
    lastUpdate = 0
    for i in range(iteration):
        newGraph = copy.deepcopy(graph)
        cut, g1, g2 = newGraph.kargerMinCut()
        if cut < minCut:
            minCut = cut
            group1 = list(g1)
            group2 = list(g2)
            lastUpdate = i
        if i - lastUpdate > n:
            # there was no better cut found in the last n loops
            # note: there is no rationale for this check, and
            #       it could be a statistical mistake to break
            break
    return minCut, group1, group2      



############################
#
#     A---3---B---2---C---3---D
#     |       |       |       |
#     2       1       1       2
#     |       |       |       |
#     E---3---F---2---G---3---H
#
# the number indicates the number of connections between 2 nodes

if __name__ == "__main__":

    graph = Graph()

    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('E')
    graph.addNode('F')
    graph.addNode('G')
    graph.addNode('H')

    graph.addEdge('A', 'B', 3)
    graph.addEdge('B', 'C', 2)
    graph.addEdge('C', 'D', 3)
    graph.addEdge('A', 'E', 2)
    graph.addEdge('B', 'F', 1)
    graph.addEdge('C', 'G', 1)
    graph.addEdge('D', 'H', 2)
    graph.addEdge('E', 'F', 3)
    graph.addEdge('F', 'G', 2)
    graph.addEdge('G', 'H', 3)

    nCut, group1, group2 = kargerMinCut(graph)
    print("# cuts =", nCut)
    print("group1 =", group1)
    print("group2 =", group2)
