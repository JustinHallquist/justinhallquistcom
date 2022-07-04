# You are given a string s
# 
# consisting of characters 0 and/or 1.
# 
# You have to remove several (possibly zero) characters from the beginning of the string, and then several (possibly zero) characters from the end of the string. The string may become empty after the removals. The cost of the removal is the maximum of the following two values:
# 
#     the number of characters 0 left in the string;
#     the number of characters 1 removed from the string. 
# 
# What is the minimum cost of removal you can achieve?
# Input
# 
# The first line contains one integer t
# (1≤t≤104
# 
# ) — the number of test cases.
# 
# Each test case consists of one line containing the string s
# (1≤|s|≤2⋅105
# 
# ), consisting of characters 0 and/or 1.
# 
# The total length of strings s
# in all test cases does not exceed 2⋅105
# 
# .
# Output
# 
# For each test case, print one integer — the minimum cost of removal you can achieve.

# The problem is poorly stated (imo) but I believe it's stating the following:
# a binary string has an implicit cost if left alone, the sum of all of the 0s
# we want to modify the string via removing from either side
# however, we incrue a cost of 1 for each 1 we remove
# so if the string was 101110110, the inplicit cost of doing nothing is 3
# if we remove the first 1 from the left side, we have a cost of 1
# we can then remove the following 0 on the left side for free
# that puts us at an implicit cost (sum of left over zeros) of 2
# we then can remove the right 0 for free, leaving the cost of the string at 1
# since we removed 1 1 and there is 1 0 left, the MAXIMUM of either of those is 1, the final value

import sys
import functools

name = "input"
path = ""

# sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def count(a, v):
    return functools.reduce(lambda memo, _v: memo + (1 if _v == v else 0), list(a), 0)

for testCase in range(1, testCases + 1):
    a = list(map(int, list(input())))

    zc = count(a, 0)
    oc = count(a, 1)

    p = []
    c = 0

    for v in a:
        if v == 0:
            c += 1
        else:
            p.append(c)

    p.append(c)

    s = []
    c = 0

    for v in a[::-1]:
        if v == 0:
            c += 1
        else:
            s.append(c)

    s.append(c)

    l = 0
    h = oc 
    a = 0

    while l <= h:
        v = False
        m = (l + h)//2
        
        for i in range(m + 1):
            lz = zc
            lz -= p[i]
            lz -= s[m - i]

            if lz <= m:
                v = True
                break

        if v:
            a = m
            h = m - 1
        else:
            l = m + 1

    print(a)

