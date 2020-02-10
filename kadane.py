"""
Kadane algorithm (Maximum subarray problem)
see https://en.wikipedia.org/wiki/Maximum_subarray_problem

example of use:
https://www.hackerrank.com/contests/w36/challenges/cut-a-strip/problem

for kadane2d, A is a 2D array
A = [[1, 2, 3], [4, 5, 6]]
A = [[1, 2, 3, 4]]
A = [[1], [2], [3], [4]]

for kadane1d, A is a 1D array
A = [1, 2, 3, 4]
"""

def kadane1d(A):
    # maximal sum in a list, Kadane 1D
    # O(N)
    # from https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    max_so_far = A[0]
    curr_max = A[0]
    for i in range(1, len(A)):
        curr_max = max(A[i], curr_max + A[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

def kadane2d(A):
    # maximal sum of a rectangular sub-array, Kadane 2D
    # O(N3)
    # see some explanation at:
    # https://stackoverflow.com/questions/9789867/the-maximal-sum-of-a-rectangular-sub-array
    N = len(A)
    M = len(A[0])
    if N == 1:
        return kadane1d(A[0])
    if M == 1:
        return kadane1d([a[0] for a in A])
    sums = [0] * M
    answer = float('-inf')
    """
    for top in range(N):
        for bottom in range(top, N):
            for i in range(M):
                sums[i] = sum([A[x][i] for x in range(top, bottom +1)])
            answer = max(answer, kadane1d(sums))
    """
    B = [a[:] for a in A]
    for row in range(1, N):
        for col in range(M):
            B[row][col] += B[row - 1][col]
    for top in range(N):
        for bottom in range(top, N):
            for i in range(M):
                sums[i] = B[bottom][i] - B[top][i] + A[top][i]
            answer = max(answer, kadane1d(sums))
    return answer

def sum_subarrays(A):
    # maximal sum of a rectangular sub-array, by brute-force
    # O(N4)
    N = len(A)
    M = len(A[0])
    maximum = float('-inf')
    for row1 in range(N):
        for col1 in range(M):
            for row2 in range(row1, N):
                for col2 in range(col1, M):
                    total = sum([sum(A[row][col1:col2 + 1]) for row in range(row1, row2 + 1)])
                    if total > maximum:
                        maximum = total
    return maximum


############################

if __name__ == "__main__":

    array = [[1, 2, 3, -1, 4, -5, 1, 1, 1]]
    print(kadane2d(array))
