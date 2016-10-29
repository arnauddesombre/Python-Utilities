# Python-Utilites
My Python 2 utility programs

Each program in this repository is stand-alone<br>
Names are self-explanatory<br>
In Python 2 but easily portable to 3 (mostly <i>xrange()</i> to <i>range()</i> and <i>print</i> to <i>print()</i>)


<b>alignment.py</b><br>
Sequence alignment:<br>
align 2 strings minimizing substitution and insertion cost<br>
parameters:<br>
penalty for substitution<br>
penalty for gap insertion<br>
return:<br>
The first string with gap inserted<br>
The second string with gap inserted<br>
The total substitution and insertion cost<br>

<b>bellman_ford.py</b><br>
Compute all shortest distances from source to all points in graph aswell as the shortest corresponding paths<br>
/!\ distances can be < 0<br>
/!\ no negative cycle<br>
return:
d = shortest distances
d[node] is the shortest distance from source to node
p = shortest path parents dictionary
p[node] is the parent of node in the shortest path from the given source

<b>dijkstra - heap - show path.py</b><br>
Compute all shortest distances from source to all points in graph as well as the shortest corresponding paths<br>
/!\ all distances must be >= 0<br>
return:<br>
shortest distances<br>
shortest path parents dictionary<br>
(implementation using heap)<br>

<b>dijkstra - heap.py</b><br>
Compute all shortest distances from source to all points in graph as well as the shortest corresponding paths<br>
/!\ all distances must be >= 0<br>
return:<br>
shortest distances<br>
(implementation using heap)<br>

<b>dijkstra - no heap.py</b><br>
Compute all shortest distances from source to all points in graph as well as the shortest corresponding paths<br>
/!\ all distances must be >= 0<br>
return:<br>
shortest distances<br>
(plain implementation)<br>

<b>find_all_paths.py</b><br>
Find all simple paths (no loop) in a graph starting from a specified node by brute recursive enumeration.<br>
Variant implemented: find only one.<br>

<b>is_prime.py</b><br>
Return a boolean indicating if a given number is prime<br>

<b>knapsack.py</b><br>
Knapsack algorithm
Value = non-negative<br>
Weight = non-negative and integral<br>
Capacity (W) = a non-negative integer<br>
2 algorithm implemented:<br>
1/ recursive algorithm, return sum of values only, but list of item can be retrieved<br>
2/ dynamic programming algorithm, return sum of values & list of items<br>

<b>prim.py</b><br>
Computes Prim's minimum spanning tree (MST) algorithm on a tree (costs can be negative)<br>

<b>traveling_salesman.py</b><br>
Computes the shortest path between all nodes of a connected graph starting at one particular node and returning at that same node (connected = there is a path between every pair of nodes)<br>
(implementation with dynamic programming algorithm)<br>
