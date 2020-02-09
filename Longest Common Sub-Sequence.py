# Longest Common Sub-Sequence

def lcseq(s1, s2):
    n1, n2 = len(s1) + 1, len(s2) + 1
    maximum = 0

    # f(i, j) = length of longest string starting at position i for s1 and j for s2
    # we are looking for f(0, 0)

    # if s1[i-1] == s2[j-1]:
    #     f(i-1, j-1) = f(i, j) + 1
    # else:
    #     f(i-1, j-1) = max { f(i, j-1) , f(i-1, j) }

    f = [[0] * n2 for i in range(n1)]

    for i in range(n1 - 1, 0, -1):
        for j in range(n2 - 1, 0, -1):
            if s1[i - 1] == s2[j - 1]:
                f[i - 1][j - 1] = f[i][j] + 1
            else:
                f[i - 1][j - 1] = max( f[i][j - 1], f[i - 1][j] )
            if f[i - 1][j - 1] > maximum:
                maximum = f[i - 1][j - 1]

    substring = ''
    if maximum > 0:
        j = 0
        for i in range(n1):
            if f[i][j] == maximum and (i == n1 - 1 or f[i + 1][j] != maximum):
                substring += s1[i]
                j += 1
                maximum -= 1
                if maximum == 0:
                    break

    return substring

            
if __name__ == "__main__":
    try:
        s1 = raw_input().strip()
        s2 = raw_input().strip()
    except:
        s1 = input().strip()
        s2 = input().strip()
    print(s1, s2)
    print(lcseq(s1, s2))
