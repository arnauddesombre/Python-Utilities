"""
Find the running median of a list of numbers

Algorithm in time O(Log(n)) using 2 heaps:
Maxheap (numbers < median); median; Minheap (numbers > median)
"""

from heapq import heappush, heappop

class Minheap:
    # direct implementation of heapq
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)

    def push(self, value):
        heappush(self.heap, value)

    def pop(self):
        if len(self.heap) == 0: raise IndexError
        return heappop(self.heap)

    def peek(self):
        return self.heap[0]


class Maxheap:
    # implementation of heapq on the inverse numbers (-x instead of x)
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)
    
    def push(self, value):
        heappush(self.heap, -value)

    def pop(self):
        if len(self.heap) == 0: raise IndexError
        return -heappop(self.heap)

    def peek(self):
        return -self.heap[0]


class Median:
    def __init__(self):
        self.maxx = Maxheap() # left heap
        self.minn = Minheap() # right heap

    def add(self, value):
        size_left = len(self.maxx)
        size_right = len(self.minn)
        if size_right == 0:
            self.minn.push(value)
        elif size_left == 0:
            right_value = self.minn.peek()
            if value <= right_value:
                self.maxx.push(value)
            else:
                self.maxx.push(self.minn.pop())
                self.minn.push(value)
        else:
            left_value = self.maxx.peek()
            right_value = self.minn.peek()
            if size_left == size_right:
                if value <= left_value:
                    self.maxx.push(value)
                else:
                    self.minn.push(value)
            elif size_left < size_right:
                if value <= right_value:
                    self.maxx.push(value)
                else:
                    self.maxx.push(self.minn.pop())
                    self.minn.push(value)
            else: # size_left > size_right
                if value >= left_value:
                    self.minn.push(value)
                else:
                    self.minn.push(self.maxx.pop())
                    self.maxx.push(value)
    
    def median(self):
        size_left = len(self.maxx)
        size_right = len(self.minn)
        if size_left < size_right:
            return self.minn.peek() * 1.
        elif size_left > size_right:
            return self.maxx.peek() * 1.
        else: # size_left == size_right
            return (self.minn.peek() + self.maxx.peek()) / 2.


############################

if __name__ == "__main__":
    
    value = [0, 1, 5, 3, 4, 9, 8]

    median = Median()
    for x in value:
        median.add(x)
        print(x, "   ", median.median())
