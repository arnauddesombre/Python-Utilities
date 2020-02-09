'''
Calculate fibonacci numbers by Matrix exponentiation

|F(n+1)| = | 1  1 | * |  F(n)  | = | 1  1 | ^ n  * | F(1) |
| F(n) |   | 1  0 |   | F(n-1) |   | 1  0 |        | F(0) |

M = [[1, 1], [1, 0]]
F(0) = F(1) = 1
calculate MEXP = M ^ n
F(n) = MEXP[1][0] + MEXP[1][1]

----
interesting application:
summation of F(x + y - z)
https://www.hackerearth.com/challenges/competitive/JNJ-3addresscode-2019/algorithm/misha-and-fibonacci-numbers-7af263da/
'''

def matmultiply(a, b, m):
    # return c = a * b where a and b are square matrices of size m
    c = [[0] * m for i in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) #% modulo
    return c

def matadd(a, b, m):
    # return c = a + b where a and b are square matrices of size m
    c = [[0] * m for i in range(m)]
    for i in range(m):
        for j in range(m):
            c[i][j] = (a[i][j] + b[i][j]) #% modulo
    return c

def matpower(a, n, m):
    # return a ^ n where a is a square matrice of size m
    answer = [[1 if i == j else 0 for i in range(m)] for j in range(m)]
    while n > 0:
        if n % 2 == 1:
            answer = matmultiply(answer, a, m)
        a = matmultiply(a, a, m)
        n = n // 2
    return answer

M = [[1, 1], [1, 0]]
#invM = [[0, 1], [1, -1]]
memoize_fibo = {}
def fibo(n):
    if n not in memoize_fibo:
        x = matpower(M, n, 2)
        return (x[1][0] + x[1][1]) #% modulo
    return memoize_fibo[n]

if __name__ == "__main__":
    for i in list(range(0, 10)) + list(range(100, 110)):
        print ("Fibonacci of", i, "=", fibo(i))
