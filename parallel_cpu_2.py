# Parallel execution using pathos / map

from time import time

from pathos.multiprocessing import cpu_count
from pathos.pools import ParallelPool

WORKERS = 4

import math
def function(n):
    """
    function arithmetic.is_prime()
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    stop = math.sqrt(n) + 1
    while i <= stop:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

# reference (1 calculation)
print("reference (1 call)")
t0 = time()
result = function(3093215881333057)
t1 = time()
T1 = t1 - t0
print(result)
print("in time =", "{0:.3f}".format(T1))
print

# parallel calculation
numbers = [3093215881333057, 3093215881333057, 3093215881333057, 3093215881333057]
print("{} parallel calculations with {} out of {} CPUs".format(len(numbers), WORKERS, cpu_count()))

t0 = time()

# create the pool of workers
pool = ParallelPool(WORKERS)

# open the functions in their own threads and return the results
results = pool.map(function, numbers)
pool.close()
pool.join()

t1 = time()
T2 = t1 - t0

print(results)
print("in time =", "{0:.3f}".format(T2))
print
print("ratio = ", "{0:.2f}%".format(100. * T2 / T1))

