def nCr(r, n, modulo):
    '''
    from:
    https://www.geeksforgeeks.org/compute-ncr-p-set-2-lucas-theorem/
    '''
    # The array C is going to store last row of pascal triangle
    # at the end. And last entry of last row is nCr
    C = [0] * (n + 1)
    # Top row of Pascal Triangle
    C[0] = 1
    # One by constructs remaining rows of Pascal Triangle from top to bottom 
    for i in range(1, (n + 1)):
        # Fill entries of current row using previous row values
        j = min(i, r)
        while(j > 0):
            C[j] = (C[j] + C[j - 1]) % modulo
            j -= 1
    return C[r]

################

def nCr(r, n, modulo):
    '''
    from:
    https://www.geeksforgeeks.org/compute-ncr-p-set-3-using-fermat-little-theorem/
    '''
    num, den = 1, 1
    for i in range(r):
        num = (num * (n - i)) % modulo
        den = (den * (i + 1)) % modulo
    return (num * pow(den, modulo - 2, modulo)) % modulo

################

def nCr(r, n):
    '''
    from:
    https://stackoverflow.com/questions/3025162/statistics-combinations-in-python/3027128
    '''
    if 0 <= r <= n:
        m = n
        ntok = 1
        ktok = 1
        for t in xrange(1, min(r, m - r) + 1):
            ntok *= n
            ktok *= t
            m -= 1
        return ntok // ktok
    else:
        return 0

################

'''
from:
https://www.quora.com/How-do-I-find-the-value-of-nCr-1000000007-for-the-large-number-n-n-10-6-in-C
'''

modulo = 10 ** 9 + 7
maxN = 10 ** 6

# pre-computations
def power(a, b, p):
    x, y = 1, a
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % p
        y = (y * y) % p
        b = b // 2
    return x % p

def modinv(n, p):
    return power(n, p - 2, p)

fact = [0] * (maxN + 1)
fact[0] = 1
for i in range(1, maxN + 1):
    fact[i] = (i * fact[i - 1]) % modulo

memoize = {}
def nCr(r, n):
    if (r, n) not in memoize:
        ret = (modinv(fact[n - r], modulo) * modinv(fact[r], modulo)) % modulo
        ret = (fact[n] * ret) % modulo
        memoize[(r, n)] = ret
    return memoize[(r, n)]
