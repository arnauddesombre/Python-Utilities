"""
knapsack algorithm
Value = non-negative
Weight = non-negative and integral
Capacity (W) = a non-negative integer

knapsack1:
recursive algorithm, return sum of values only, but list of item can be retrieved
knapsack2:
dynamic programming algorithm, return sum of values & list of items
"""
weight = [] # weight of each item, in list format
value = []  # value of each item, in list format

import sys
sys.setrecursionlimit(1000000)

A = {}
def knapsack1(W, n=-1):
    # n = total number of item available
    # W = weight capacity
    if n == -1:
        n = len(weight) - 1
    if n == 0:
        return 0
    if n not in A:
        A[n] = {}
    if W not in A[n]:
        if weight[n] > W:
            solution = knapsack1(W, n - 1)
        else:
            solution = max(knapsack1(W, n - 1),
                           knapsack1(W - weight[n], n - 1) + value[n])
        A[n][W] = solution
    else:
        solution = A[n][W]
    return solution

import numpy as np

def knapsack2(W):
    # n = total number of item available
    # W = weight capacity
    n = len(weight) - 1
    # define n+1 * W+1 array of 0 (integer)
    A = np.zeros((n+1, W+1), dtype=np.int)
    for x in xrange(0, W+1):
        A[0][x] = 0
    for i in xrange(1, n+1):
        for x in xrange(0, W+1):
            if weight[i] > x:
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-weight[i]] + value[i])
    item = []
    w = W
    for i in range(n, 0, -1):
        if A[i][w] != A[i-1][w]:
            item.append(i)
            w -= weight[i]
    return A[n][W], item


############################
# Note:
# value[0] = 0 (unused)
# weight[0] = 0 (unused)
# len(weight) = len(weight) = numberItem + 1

sizeKnapsack, numberItem = 6, 4
value  = [0, 3, 2, 4, 4]
weight = [0, 4, 3, 2, 3]

# recursive algorithm
############################
print
print knapsack1(sizeKnapsack)
# retrieve list of item
item = []
w = sizeKnapsack
for i in range(numberItem, 0, -1):
    if i-1 in A and A[i][w] != A[i-1][w]:
        item.append(i)
        w -= weight[i]
print item

# dynamic programming algorithm
############################
print
A, item = knapsack2(sizeKnapsack)
print A
print item
print
