"""
contains:
is_prime(n):            Return boolean indicating if n is prime
gcd(a, b):              Return greatest common divisor of a and b
gcdm(*args):            Return gcd of args
lcm(a, b):              Return lowest common multiple of a and b
lcmm(*args):            Return lcm of args
prime_decomposition(n): Return all the prime factors of n in a list
factors(n):             Return all the factors (divisors) of n in a list
"""

from math import sqrt
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
    stop = sqrt(n) + 1
    while i <= stop:
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

def lcmm(*args):
    """
    Return lcm of args
    """   
    return reduce(lcm, args)

# Prime decomposition, from:
# https://rosettacode.org/wiki/Prime_decomposition#Python

from math import floor, sqrt
try: 
    long
except NameError: 
    long = int
 
def prime_decomposition(n):
    """
    Return all the prime factors of n in a list
    """   
    step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
    maxq = long(floor(sqrt(n)))
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
    for x in xrange(1, int(sqrt(n)) + 1):
      if n % x == 0:
        f.add(x)
        f.add(n // x)
    return sorted(f)

############################

if __name__ == "__main__":
    
    print
    print gcdm(10, 20, 30, 45)
    print lcmm(10, 20, 30, 45)
    print
    tocalc =  2**59 - 1
    print("%s = %s" % (tocalc, prime_decomposition(tocalc)))
    tocalc =  100
    print("%s = %s" % (tocalc, prime_decomposition(tocalc)))
    print
    print factors(12345678)

    # some prime numbers from:
    # https://en.wikipedia.org/wiki/List_of_prime_numbers
    print
    print is_prime(17)
    print is_prime(999331)
    print is_prime(2147483647)
    print is_prime(63018038201)
    print is_prime(3093215881333057)
    print
