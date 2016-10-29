"""
sequence alignment
align 2 strings minimizing substitution and insertion cost

parameters:
penalty for substitution
penalty for gap insertion

return:
[0] = first string with gap inserted
[1] = second string with gap inserted
[2] = total substitution and insertion cost
"""
gap = '_'
penaltySubstitution = 0.5
penaltyGap = 1.0

import sys
sys.setrecursionlimit(1000000)

Dic = {}
def align(string1, string2):
    if string1 == '':
        s1 = gap * len(string2)
        return [s1, string2, penaltyGap * len(string2)]
    if string2 == '':
        s2 = gap * len(string1)
        return [string1, s2, penaltyGap * len(string1)]
    if (string1, string2) in Dic:
        return Dic[(string1, string2)]
    if string1[0] == string2[0]:
        a = align(string1[1:], string2[1:])
        Dic[(string1, string2)] = a
        return [string1[0] + a[0], string2[0] + a[1], a[2]]
    else:
        a1 = align(string1, string2[1:])
        a2 = align(string1[1:], string2)
        a3 = align(string1[1:], string2[1:])
        a1[2] += penaltyGap
        a2[2] += penaltyGap
        a3[2] += penaltySubstitution
        if a1[2] <= min(a2[2], a3[2]):
            solution = [gap + a1[0], string2[0] + a1[1], a1[2]]
        elif a2[2] <= min(a1[2], a3[2]):
            solution = [string1[0] + a2[0], gap + a2[1], a2[2]]
        else: # a3[2] <= min(a1[2], a2[2])
            solution = [string1[0] + a3[0], string2[0] + a3[1], a3[2]]
        Dic[(string1, string2)] = solution
        return solution


############################

string1 = "AGAATCTAGACTGAATTCGCG"
string2 = "AGTACTGAACTTAGGATTTACG"

a = align(string1, string2)

print
print string1
print string2
print
print a[0]
print a[1]
print
print "cost =", a[2]
print
