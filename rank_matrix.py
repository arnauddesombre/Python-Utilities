'''
Find the rank of a matrix

https://www.geeksforgeeks.org/program-for-rank-of-matrix/
'''

def swapRows(a, row1, row2):
    a[row2], a[row1] = a[row1], a[row2]
    return a

def matrixRank(a):
    if a == []:
        return 0
    nrow = len(a)
    ncol = len(a[0])
    # transpose the matrix if nrow < ncol
    if nrow < ncol:
        b = []
        for m in range(ncol):
            l = []
            for n in range(nrow):
                l.append(a[n][m])
            b.append(l)
        a = b
        ncol, nrow = nrow, ncol
    rank = ncol
    for row in range(rank):
        if a[row][row] != 0:
            for col in range(nrow):
                if col != row:
                    x = a[col][row] / a[row][row]
                    for i in range(rank):
                        a[col][i] -= x * a[row][i]
        else:
            reduce = True
            for i in range(row + 1, nrow):
                if a[i][row] != 0:
                    a = swapRows(a, row, i)
                    reduce = False
                    break
            if reduce:
                rank -= 1
                for i in range(nrow):
                    a[i][row] = a[i][rank]
            row -= 1
    return rank

if __name__ == "__main__":
    a = [[0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 0, 1, 0]]
    print(matrixRank(a))
