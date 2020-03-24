'''
Segment Tree

For more information, see:
https://www.commonlounge.com/discussion/58e0c0af5d1f487c9942f4625bfd4cc2
http://codeforces.com/blog/entry/18051
https://www.dropbox.com/s/m2jnbd8gkoz7en1/segtree.pdf?dl=0

Note:
this algorithm is tested (in C++). see:
https://www.spoj.com/submit/FREQUENT/id=22560461
(sign-in to see the code)
'''

# define 'combine' and 'extrema'

# MINIMUM:
combine = lambda x, y: min(x, y)
extrema = float('inf')

'''
# MAXIMUM:
combine = lambda x, y: max(x, y)
extrema = -float('inf')
'''

'''
# SUM:
combine = lambda x, y: x + y
extrema = 0
'''

'''
# BITWISE XOR:
combine = lambda x, y: x ^ y
extrema = 0
'''

'''
# BOOLEAN XOR:
from operator import xor
combine = lambda x, y: xor(bool(x), bool(y))
extrema = false
'''

'''
# USING CLASS
# for example, see submission to https://www.spoj.com/problems/FREQUENT/
class Node():
    __slots__ = ['value1', 'value2']
    def __init__(self, args):
        self.value1 = args[0]
        self.value2 = args[1]
    def update(self, args):
        self.value1 = args[0]
        self.value2 = args[1]
    def enum(self):
        return [self.left_value, self.left_count, self.right_value, self.right_count, self.best_count]

def combine(l, r):
    return l.value1 + r.value1
'''

def construction(array, n):
    data = [None] * n + array
    for idx in range(n - 1, 0, -1):
        data[idx] = combine(data[2 * idx], data[2 * idx + 1])
    return data

def update(data, n, idx, value):
    idx += n
    data[idx] = value
    while idx > 1:
        idx //= 2
        data[idx] = combine(data[2 * idx], data[2 * idx + 1])
    return data

def query(data, n, left, right):
    # applies 'combine' to the elements of A
    # (such as data = construction(A))
    # from left (*included*) to right (*excluded*)
    # NOTE: data[1] always contains the 'combine'
    #       value for all the elements of A
    left += n
    right += n
    resl = extrema
    resr = extrema
    while left < right:
        if left % 2 == 1:
            resl = combine(resl, data[left])
            left += 1
        if right % 2 == 1:
            right -= 1
            resr = combine(data[right], resr)
        left //= 2
        right //= 2
    res = combine(resl, resr)
    return res

if __name__ == '__main__':
    #    0  1  2  3  4  5  6  7
    A = [1, 5, 3, 7, 3, 2, 5, 7]
    n = len(A)
    segment = construction(A, n)
    print((segment, n, 1, 7))
    segment = update(segment, n, 5, 6)
    print(query(segment, n, 1, 7))
