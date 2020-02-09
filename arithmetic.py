"""
contains:
is_prime(n):            Return boolean indicating if n is prime
gcd(a, b):              Return greatest common divisor of a and b
gcdm(*args):            Return gcd of args
lcm(a, b):              Return lowest common multiple of a and b
lcmm(*args):            Return lcm of args
prime_decomposition(n): Return all the prime factors of n in a list
factors(n):             Return all the factors (divisors) of n in a list


Number theory with Python:
http://www.math.umbc.edu/~campbell/Computers/Python/numbthy.html
"""

def isqrt(n):
    '''
    return the interger square root of i
    (the largest integer a such that a ** 2 <= x)
    using Newton's method
    '''
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def is_prime(n):
    """
    Return boolean indicating if a given number is prime

    from Wikipedia:
    https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def gcd(a, b):
    """
    Return greatest common divisor

    NOTE:
    gcd() is native in the fractions module:
    from fractions import gcd
    """
    while b:      
        a, b = b, a % b
    return a

from functools  import reduce
def gcdm(*args):
    """
    Return gcd of args
    """   
    return reduce(gcd, args)

def lcm(a, b):
    """
    Return lowest common multiple
    """
    return (a * b) // gcd(a, b) if (a and b) else 0

from functools  import reduce
def lcmm(*args):
    """
    Return lcm of args
    """   
    return reduce(lcm, args)

# Prime decomposition, from:
# https://rosettacode.org/wiki/Prime_decomposition#Python

from math import sqrt
def prime_decomposition(n):
    """
    Return all the prime factors of n in a list
    """   
    step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
    maxq = int(sqrt(n)) + 1
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + prime_decomposition(n // q) or [n]

from math import sqrt
def factors(n):
    """
    Return all the factors (divisors) of n
    """   
    f = set()
    step = 2 if n % 2 else 1
    for x in range(1, int(sqrt(n)) + 1, step):
      if n % x == 0:
        f.add(x)
        f.add(n // x)
    return sorted(list(f))

# divisors of n from prime factors
# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

from math import sqrt
from itertools import compress

def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2:: i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]

def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primeslist:
      if p * p > n : break
      count = 0
      while not n % p:
        n //= p
        count += 1
      if count > 0: pf.append((p, count))
    if n > 1: pf.append((n, 1))
    return pf

def divisors(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x * p ** k for k in range(1, e + 1) for x in divs]
    return divs

############################

if __name__ == "__main__":
    
    print(gcdm(10, 20, 30, 45))
    print(lcmm(10, 20, 30, 45))
    print()
    tocalc =  2**59 - 1
    print("%s = %s" % (tocalc, prime_decomposition(tocalc)))
    tocalc =  100
    print("%s = %s" % (tocalc, prime_decomposition(tocalc)))
    print()
    print(factors(12345678))

    n = 600851475143
    primeslist = primes(int(n**0.5)+1) 
    print(divisors(n))

    # some prime numbers from:
    # https://en.wikipedia.org/wiki/List_of_prime_numbers
    print()
    print(is_prime(17))
    print(is_prime(999331))
    print(is_prime(2147483647))
    print(is_prime(63018038201))
    print(is_prime(3093215881333057))
    print()
