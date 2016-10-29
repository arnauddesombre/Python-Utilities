"""
return boolean indicating if a given number is prime

from Wikipedia:
https://en.wikipedia.org/wiki/Primality_test
"""
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    stop = int(n ** 0.5) + 1
    while i <= stop:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


############################
# some prime numbers from:
# https://en.wikipedia.org/wiki/List_of_prime_numbers

print
print is_prime(17)
print is_prime(999331)
print is_prime(2147483647)
print is_prime(63018038201)
print is_prime(3093215881333057)
print
