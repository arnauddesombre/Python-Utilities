# determine the convex hull of a set of points (Graham scan algorithm)

# see Coursera - Algorithms, part I / Week 2 - Stacks and Queues
# and http://www2.lawrence.edu/fast/GREGGJ/CMSC210/convex/convex.html

import math

class Point:
    def __init__(self, ref, x, y):
        self.ref = ref
        self.x = x
        self.y = y
        self.polarAngle = 0.
    def setPolarAngle(self, polarAngle):
        self.polarAngle = polarAngle
    def computePolarAngle(self, other):
        return math.atan2(self.y - other.y, self.x - other.x)
    def direction(self, a, b, c):
        area = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
        if area < 0:
            return -1
        elif area > 0:
            return 1
        else:
            return 0

# read points from points.txt
points = []
ref = 0
with open("convex_hull.txt") as f:
    for line in f:
        x, y = map(float, line.split())
        points.append(Point(ref, x, y))
        ref += 1
f.close()

if len(points) < 2:
    raise ValueError("there should be at least 2 points")

# determine lowest y
points = sorted(points, key=lambda point: point.y)

# compute polar angle from points[0] (lowest y), and sort by polarAngle
for point in points[1:]:
    point.setPolarAngle(point.computePolarAngle(points[0]))
points = sorted(points, key=lambda point: point.polarAngle)

# determine convex hull
hull = []
hull.append(points[0])
hull.append(points[1])

for i in range(2, len(points)):
    top = hull.pop()
    while top.direction(hull[-1], top, points[i]) <= 0:
           top = hull.pop()
    hull.append(top)
    hull.append(points[i])

print("The points belonging to the convex hull are:")
print("Line\tX\tY")
for point in hull:
    print("%3i\t%.2f\t%.2f" % (point.ref, point.x, point.y))
# (line starts at zero: line reference in points.txt)


#################
# graphical representation

import numpy as np
import matplotlib.pyplot as plt

x, y = [], []
for point in points:
    x.append(point.x)
    y.append(point.y)
plt.scatter(x, y, c='b', marker='o')

x, y = [], []
for point in hull:
    x.append(point.x)
    y.append(point.y)
plt.scatter(x, y, c='r', marker='x')

plt.show()    

        
        
            
