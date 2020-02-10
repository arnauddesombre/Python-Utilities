"""
sequence alignment
align 2 strings minimizing substitution and insertion cost

parameters:
string #1
string #2
penalty for substitution (default = 1.)
penalty for gap insertion (default = 1.)

return:
[0] = first string with gaps inserted (gap = ".")
[1] = second string with gaps inserted (gap = ".")
[2] = total substitution and insertion cost
"""

gap = "."
penaltySubstitution_ = 1.
penaltyGap_ = 1.

import sys
sys.setrecursionlimit(1000000)

dic = {}
def align(string1, string2, penaltyGap=penaltyGap_, penaltySubstitution=penaltySubstitution_):
    if (string1, string2) in dic:
        return dic[(string1, string2)]
    if string1 == "":
        s1 = gap * len(string2)
        solution = [s1, string2, penaltyGap * len(string2)]
    elif string2 == "":
        s2 = gap * len(string1)
        solution = [string1, s2, penaltyGap * len(string1)]
    elif string1[0] == string2[0] or string1[0] == gap or string2[0] == gap:
        a = align(string1[1:], string2[1:], penaltyGap, penaltySubstitution)
        solution = [string1[0] + a[0], string2[0] + a[1], a[2]]
    else:
        a1 = align(gap + string1, string2, penaltyGap, penaltySubstitution)
        a2 = align(string1, gap + string2, penaltyGap, penaltySubstitution)
        a3 = align(string1[1:], string2[1:], penaltyGap, penaltySubstitution)
        a1[2] += penaltyGap
        a2[2] += penaltyGap
        a3[2] += penaltySubstitution 
        if a1[2] <= min(a2[2], a3[2]):
            solution = a1
        elif a2[2] <= min(a1[2], a3[2]):
            solution = a2
        else: # a3[2] <= min(a1[2], a2[2])
            solution = [string1[0] + a3[0], string2[0] + a3[1], a3[2]]
    dic[(string1, string2)] = solution
    return solution

############################

if __name__ == "__main__":
    
    string1 = "AGAATCTAGACTGAATTCGCG"
    string2 = "AGTACTGAACTTAGGATTTACG"

    # disallow substitution:
    a = align(string1, string2, 1., float("inf"))

    print()
    print(string1)
    print(string2)
    print()
    print(a[0])
    print(a[1])
    print()
    print("cost =", a[2])
    print()
