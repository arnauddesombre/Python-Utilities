# Python-Utilities
My Python 2 utility programs

Each program in this repository is a stand-alone file.<br>
In Python 2 but easily portable to Python 3 (change <i>xrange(...)</i> to <i>range(...)</i> and <i>print ...</i> to <i>print(...)</i>).

-----------------------

<b>alignment.py</b><br>
Sequence alignment: align 2 strings minimizing substitution and insertion cost.<br>
Parameters:
- penalty for substitution<br>
- penalty for gap insertion<br>

Return:
- The first string with gap inserted<br>
- The second string with gap inserted<br>
- The total substitution and insertion cost<br>

-----------------------

<b>bellman_ford.py</b><br>
Compute all shortest distances from source to all points in graph as well as the shortest corresponding paths using the Bellman-Ford algorithm.<br>
/!\ distances can be < 0<br>
/!\ no negative cycle can exist in the tree<br>

Return:
- shortest distances<br>
- shortest path parents dictionary<br>
- generates an error if a negative cycle exists<br>

-----------------------

<b>dijkstra - heap - show path.py</b><br>
Compute all shortest distances from source to all points in graph as well as the shortest corresponding paths using Dijkstra's algorithm.<br>
/!\ all distances must be >= 0<br>
(implementation using heap)<br>

Return:
- shortest distances<br>
- shortest path parents dictionary<br>

-----------------------

<b>dijkstra - heap.py</b><br>
Compute all shortest distances from source to all points in graph using Dijkstra's algorithm.<br>
/!\ all distances must be >= 0<br>
(implementation using heap)<br>

Return:
- shortest distances<br>

-----------------------

<b>dijkstra - no heap.py</b><br>
Compute all shortest distances from source to all points in graph using Dijkstra's algorithm.<br>
/!\ all distances must be >= 0<br>
(plain implementation)<br>

return:
- shortest distances<br>

-----------------------

<b>find_all_paths.py</b><br>
Find all simple paths (no loop) in a graph starting from a specified node by brute recursive enumeration.<br>
Variant implemented: find only one.<br>

-----------------------

<b>is_prime.py</b><br>
Return a Boolean indicating if a given number is prime.<br>

-----------------------

<b>knapsack.py</b><br>
Knapsack algorithm (Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible).
- Value = non-negative<br>
- Weight = non-negative and integral<br>
- Total weight limit = a non-negative integer<br>

2 algorithm implemented:<br>
1/ recursive algorithm, return sum of values only, but list of item can be retrieved<br>
2/ dynamic programming algorithm, return sum of values & list of items<br>

-----------------------

<b>prim.py</b><br>
Computes Prim's minimum spanning tree (MST) algorithm on a tree (edge's costs can be negative).<br>

-----------------------

<b>traveling_salesman.py</b><br>
Computes the shortest path between all nodes of a connected graph starting at one particular node and returning at that same node (connected = there is a path between every pair of nodes).<br>
(implementation with dynamic programming algorithm)

-----------------------
