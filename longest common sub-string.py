# Longest Common Sub-String

def lcstr(s1, s2):
    n1, n2 = len(s1) + 1, len(s2) + 1
    index, maximum = None, 0

    # f(i, j) = longest string ending at position i for s1 and j for s2
    # we are looking for max{f(i, j)} with 0 <= i < n1 and 0 <= j < n2
    # f(i+1, j+1) = f(i, j) + 1 if s1[i+1] == s2[j+1] else 0

    f = [[0] * n2 for i in range(n1)]

    for i in range(1, n1):
        for j in range(1, n2):
            if s1[i - 1] == s2[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
                if f[i][j] > maximum:
                    maximum = f[i][j]
                    index = i - 1
            else:
                f[i][j] = 0

    if index != None:
        substring = s1[index - maximum + 1: index + 1]
    else:
        substring = ''
    return substring

            
if __name__ == "__main__":
    try:
        s1 = raw_input().strip()
        s2 = raw_input().strip()
    except:
        s1 = input().strip()
        s2 = input().strip()
    print('S1:', s1)
    print('S2:', s2)
    print(lcstr(s1, s2))
