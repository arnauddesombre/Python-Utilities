# Parallel execution using multiprocessing/map

# /!\
# this does not work with any function
# if you replace function() with is_prime() from arithmetic.py
# for example, this will not work, as it uses CPU...
# for further explanation, see:
# https://stackoverflow.com/questions/26432411/multiprocessing-dummy-in-python-is-not-utilising-100-cpu

# see parallel_cpu_2.py for pathos implementation

from time import time
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool

WORKERS = 6

def function(n):
    T = 3
    sleep(T)
    return "Slept for {} seconds with input {}".format(T, n)

# reference (1 calculation)
print("reference (1 call)")
t0 = time()
result = function(0)
t1 = time()
T1 = t1 - t0
print(result)
print("in time =", "{0:.3f}".format(T1))
print()

# parallel calculation
print("parallel calculations")

numbers = [1, 2, 3, 4, 5, 6]
t0 = time()

# create the pool of workers
pool = ThreadPool(WORKERS)

# open the functions in their own threads and return the results
results = pool.map(function, numbers)
pool.close()
pool.join()

t1 = time()
T2 = t1 - t0

print(results)
print("in time =", "{0:.3f}".format(T2))
print()
print("ratio = ", "{0:.2f}%".format(100. * T2 / T1))

