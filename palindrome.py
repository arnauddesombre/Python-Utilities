"""
Find longest palindrome within a string
Manacher's algorithm

source:
https://articles.leetcode.com/longest-palindromic-substring-part-i/
https://articles.leetcode.com/longest-palindromic-substring-part-ii/
"""

# Transform S into T
# For example, S = "abba" -> T = "^#a#b#b#a#$"
# ^ and $ signs are sentinels appended to each end to avoid bounds checking
def preProcess(s):
    n = len(s)
    if (n == 0):
        return "^$"
    ret = "^"
    for i in range(n):
        ret += "#" + s[i]
    ret += "#$"
    return ret;
 
def longestPalindrome(s):
    T = preProcess(s)
    n = len(T)
    P = [0] * n
    C = 0
    R = 0
    for i in range(1, n - 1):
        i_mirror = 2 * C - i  # equals to i' = C - (i-C)
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
        # If palindrome centered at i expands past R,
        # adjust center based on expanded palindrome
        if i + P[i] > R:
            C = i
            R = i + P[i]
    # Find the maximum element in P
    maxLen = 0
    centerIndex = 0
    for i in range(1, n - 1):
        if P[i] > maxLen:
            maxLen = P[i]
            centerIndex = i
    x = (centerIndex - 1 - maxLen) // 2
    return s[x: x + maxLen]

############################

if __name__ == "__main__":
    string = "a man a plan a canal panama"
    string = string.replace(' ', '')
    print("string            :", string)
    print("longest palindrome:", longestPalindrome(string))
