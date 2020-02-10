# Python utilities
My Python utility programs.<br>

Each program in this repository is a stand-alone file, and works in Python 2 and 3. These can be useful for competitive programming for example.<br>

Tip to import a homemade method in another python program:
```
# import function bellman_ford() from C:/temp/bellman_ford.py

import imp
BF = imp.load_source("bellman_ford", "C:/temp/bellman_ford.py")
...
x = BF.bellman_ford(graph, node)
```

----------

<b>alignment.py </b><br>
<b>alignment v2.py</b><br>
Sequence alignment (align 2 strings minimizing substitution and insertion cost).<br>
Optional parameters:
- penalty for substitution<br>
- penalty for gap insertion<br>

Return:
- The first string with gap inserted<br>
- The second string with gap inserted<br>
- The total substitution and insertion cost<br>

----------

<b>arithmetic.py</b><br>
Contain the following arithmetic functions:<br>
- is_prime(n): return Boolean indicating if n is prime
- gcd(a, b): return greatest common divisor of a and b
- gcdm(*args): return gcd of args
- lcm(a, b): return lowest common multiple of a and b
- lcmm(*args): return lcm of args
- prime_decomposition(n): return all the prime factors of n in a list
- factors(n): return all the factors (divisors) of n in a list (brute-force from 1 to sqrt(n))
- divisors(n): same as factors(n), using combination of prime factors (much more efficient)<br>

----------

<b>ASCII.py</b><br>
ASCII codes using Unicode strings (for example print(u'\u2588') will print ASCII character 0xDB (FULL BLOCK))<br>

----------

<b>a-star - show path.py</b><br>
Compute the shortest distance from a source to a destination in a directed graph where some crow distance ([Euclid](https://en.wikipedia.org/wiki/Euclidean_distance) or [haversine](https://en.wikipedia.org/wiki/Haversine_formula) can be defined as well as the shortest corresponding path.<br>
/!\ all distances must be >= 0<br>

Return:
- shortest distance<br>
- shortest path from source to destination<br>

Note: this program implements A\* starting from the Dijkstra implementation of "dijkstra - show path.py"<br>

----------

<b>a-star.py</b><br>
Compute the shortest distance from a source to a destination in a directed graph where some crow distance ([Euclid](https://en.wikipedia.org/wiki/Euclidean_distance) or [haversine](https://en.wikipedia.org/wiki/Haversine_formula) can be defined.<br>
/!\ all distances must be >= 0<br>

Return:
- shortest distance<br>

Note: this program implements A\* starting from the Dijkstra implementation of "dijkstra.py"<br>

----------

<b>bellman_ford.py</b><br>
Compute all shortest distances from a source to all points in a directed graph as well as the shortest corresponding paths using the Bellman-Ford algorithm.<br>
/!\ distances can be < 0<br>
/!\ no negative cycle can exist in the tree<br>

Return:
- shortest distances<br>
- shortest path parents dictionary<br>
- Boolean indicating if a negative cycle exists<br>

negative_cycle(graph, source) will return a list containing one negative cycle (note there can be multiple negative cycles). The first
and last element of the list are the same ([A, B, ..., A])<br>

bellman_ford_path(parents, source, destination) will return the path (a list) from 'source' to 'destination'. Note that if there is a negative loop, this function will run indefinitely<br>

----------

<b>bfs.py</b><br>
Explore a directed graph using Breadth First Search (BFS).<br>

Return:
- a dictionary containing the visiting order for each node starting at 1<br>

----------

<b>bidirectional a-star - show path.py</b><br>
compute the shortest distance from a source to a destination in a directed graph where some crow distance ([Euclid](https://en.wikipedia.org/wiki/Euclidean_distance) or [haversine](https://en.wikipedia.org/wiki/Haversine_formula) can be defined as well as the shortest corresponding path using bi-directional A\* algorithm.<br>
/!\ all distances must be >= 0<br>

Return:
- shortest distance<br>
- shortest path from source to destination<br>

----------

<b>bidirectional dijkstra - show path.py</b><br>
compute the shortest distance from a source to a destination in a directed graph as well as the shortest corresponding path using bi-directional Dijkstra algorithm.<br>
/!\ all distances must be >= 0<br>

Return:
- shortest distance<br>
- shortest path from source to destination<br>

----------

<b>binaryIndexedTree.py</b><br>
Implementation of Binary Indexed Trees (Fenwick Tree).<br>

----------

<b>centroid.py</b><br>
Implementation of the Centroid Decomposition of a Tree.<br>
This program should be provided the text file centroid.txt as input<br>
<i>python centroid.py < centroid.txt</i><br>

----------

<b>clustering.py</b><br>
Compute k clusters from an undirected graph, using Kruskal's MST (minimum spanning tree) algorithm, so that the minimum distance between 2 nodes in different clusters is maximized.<br>

Return:
- a dictionary of integer keys 1 to k containing the list of nodes of each cluster<br>
- the minimum distance between the k clusters<br>

----------

<b>combinations.py</b><br>
Miscellaneous implementations of “n choose r” nCr(), with optimizations for competitive programming.<br>

----------

<b>compare a-star & landmark [roadmap]</b><br>
Compare the performance of A\* and Landmarks algorithm using real world maps (links and instructions are in the file, or also available on this page: USA-road-d.NY.co and USA-road-d.NY.gr).<br>
v1: The landmarks used are the nodes closest to the 4 corners of the square and the 4 centers of each side of the square of the square that contains the map.<br>
v2: The landmarks used are the nodes closest to the 4 corners of the square, the 4 centers of each side of the square, and the 8 quarters (2 per side) of the square that contains the map. Only the 4 best landmarks among the 16 are used for each calculation.<br>

<b>compare dijkstra & a-star.py</b><br>
Compare the performance of Dijkstra, bidirectional Dijkstra, A\* algorithm, and Bellman-Ford, using a N * N square where roads are all vertical and all horizontal lines.<br>

<b>compare dijkstra & a-star [roadmap].py</b><br>
Compare the performance of Dijkstra, bidirectional Dijkstra, and A\* algorithm, using real world maps (links and instructions are in the file).<br>

These are not a "utility" files, just performance and calibration tools. The conclusion is similar to what's described in:<br>
http://www.cs.princeton.edu/courses/archive/spr06/cos423/Handouts/EPP%20shortest%20path%20algorithms.pdf<br>
- in a graph where no crow distance can be defined (social network for example), bi-directional Dijkstra is best<br>
- if a crow distance can be defined, A\* is best (bi-directional A\* is not as good - but still better than bi-directional Dijkstra)<br>
- using landmarks requires more memory (storage) and some pre-processing. Landmark v1 is faster than A\* by by 25-30%, Landmark v2 is faster by 35-40%<br>

----------

<b>convex hull.py</b><br>
Determine the convex hull of a set of points using Graham scan algorithm.
This program should be provided the text file convex_hall.txt as input<br>
<i>python "convex hall.py" < convex_hall.txt</i><br>

----------

<b>dfs.py</b><br>
Explore a directed graph using Depth First Search (DFS).<br>
Implements:<br>
- DFS_recursive(graph, source): a recursive algorithm<br>
- DFS_linear(graph, source): a linear algorithm<br>
- DFS(graph, source, recursive=False): which calls one or the other<br>

Return:
- 2 dictionaries containing the visiting orders (pre_visit & post_visit) for each node starting at 1<br>

----------

<b>dijkstra - show path.py</b><br>
Compute all shortest distances from a source to all nodes in a directed graph as well as the shortest corresponding paths using Dijkstra's algorithm.<br>
/!\ all distances must be >= 0<br>

Return:
- shortest distances<br>
- shortest path parents dictionary<br>

(if a destination is specified, the algorithm stops when 'destination' is found and only returns the distance from source to destination as well as the corresponding shortest path.)

----------

<b>dijkstra.py</b><br>
Compute all shortest distances from a source to all nodes in a directed graph using Dijkstra's algorithm.<br>
/!\ all distances must be >= 0<br>

Return:
- shortest distances<br>

(if a destination is specified, the algorithm stops when 'destination' is found and only returns the distance from source to destination.)<br>

----------

<b>fibonacci.py</b><br>
Calculate the Fibonacci numbers using Matrix exponentiation.<br>

----------

<b>find_all_paths.py</b><br>
Find all simple paths (no loop) in a directed graph starting from a specified node by brute recursive enumeration.<br>
Variant implemented: find only one.<br>

----------

<b>floyd-warshall.py</b><br>
Implementation of the Floyd-Warshall algorithm (all-pairs shortest paths).<br>

----------

<b>kadane.py</b><br>
Implementation of the Kadane algorithm (Maximum subarray problem).<br>

----------

<b>kargerMinCut.py</b><br>
Computes the minimum cut of an undirected graph using Karger's algorithm.<br>

----------

<b>knapsack.py</b><br>
Knapsack algorithm (Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible).
- Value = non-negative<br>
- Weight = non-negative and integral<br>
- Total weight limit = a non-negative integer<br>

2 algorithm implemented:<br>
1/ recursive algorithm, return sum of values only, but list of item can be retrieved<br>
2/ dynamic programming algorithm, return sum of values & list of items<br>

----------

<b>kruskal.py</b><br>
Computes Kruskal's minimum spanning tree (MST) algorithm of an undirected graph (edge's costs can be negative).<br>

----------

<b>landmark - show path.py</b><br>
compute the shortest distance from a source to a destination in a directed graph where some crow distance (Euclid) can be defined, and where distances from some landmarks are known, as well as the shortest corresponding path.<br>
/!\ all distances must be >= 0<br>

Return:
- shortest distance<br>
- shortest path from source to destination<br>

----------

<b>lca.py</b><br>
Miscellaneous implementation of Lowest Common Ancestor algorithms, with optimizations for competitive programming.<br>
This program should be provided the text file lca.txt as input<br>
<i>python lca.py < lca.txt</i><br>

----------

<b>longest common sub-sequence.py</b><br>
<b>longest common sub-string.py</b><br>
Determine the longest sub-sequence / sub-string between two sequences (strings).<br>
This program should be provided the text file "longest common sub.txt" as input<br>
<i>python "longest common sub-sequence.py" < "longest common sub.txt"</i><br>

a sub-string is a contiguous part of a string (AB is a sub-string of ABABA).<br>
a sub-sequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements (AAA is a sub-string of ABABA).<br>

----------

<b>palindrome.py</b><br>
Find the longest palindrome within a string, using Manacher's algorithm.<br>

----------

<b>parallel_cpu_1.py</b><br>
<b>parallel_cpu_2.py</b><br>

1: Parallel execution using multiprocessing/map<br>
<i>from multiprocessing.dummy import Pool as ThreadPool</i><br>

2: Parallel execution using pathos/map<br>
<i>from pathos.multiprocessing import cpu_count</i><br>
<i>from pathos.pools import ParallelPool</i><br>

----------

<b>prim.py</b><br>
Computes Prim's minimum spanning tree (MST) algorithm of an undirected graph (edge's costs can be negative).<br>

----------

<b>rank_matrix.py</b><br>
Find the rank of a matrix (not necessarily square).<br>

----------

<b>running_median.py</b><br>
Computes the running median of a series of numbers in O(Log(n)) time, which is the most efficient algorithm.<br>

----------

<b>scc.py</b><br>
Strongly Connected Components (SCC)<br>
Compute the SCC of a directed graph using the Kosaraju's algorithm<br>

return:
- the number of SCC<br>
- a dictionary SCC1, SCC1[n] = list of all nodes in SCC number 'n'<br>
- a dictionary SCC2, SCC2[node] = number of the SCC of which 'node' is a member<br>

----------

<b>segment_tree.py</b><br>
Implementation of Segment Tree.<br>

----------

<b>traveling_salesman.py</b><br>
Computes the shortest path between all nodes of a connected graph starting at one particular node and returning at that same node (connected = there is a path between every pair of nodes).<br>
(implementation with dynamic programming algorithm)<br>

----------

<b>trie.py</b><br>
Implementation of a TRIE<br>

----------

<b>weekday.py</b><br>
isleap(year) return a Boolean indicating if the year is leap<br>
weekday(day, month, year) return the day of the week for any date<br>

Note that the periodicity of weekday is 2800 years. i.e:<br>
weekday(day, month, year) == weekday(day, month, year + 2800) for any date<br>

----------
