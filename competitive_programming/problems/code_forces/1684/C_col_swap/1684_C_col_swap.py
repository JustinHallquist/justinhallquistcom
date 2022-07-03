# You are given a grid with n rows and m columns, where each cell has a positive integer written on it. Let's call a grid good, if in each row the sequence of numbers is sorted in a non-decreasing order. It means, that for each 1≤i≤n and 2≤j≤m the following holds: ai,j≥ai,j−1
# 
# .
# 
# You have to to do the following operation exactly once: choose two columns with indexes i
# and j (not necessarily different), 1≤i,j≤m
# 
# , and swap them.
# 
# You are asked to determine whether it is possible to make the grid good after the swap and, if it is, find the columns that need to be swapped.
# Input
# 
# Each test contains multiple test cases. The first line contains the number of test cases t
# (1≤t≤100
# 
# ). Description of the test cases follows.
# 
# The first line of each test case contains two integers n
# and m (1≤n,m≤2⋅105
# 
# ) — the number of rows and columns respectively.
# 
# Each of the next n
# rows contains m integers, j-th element of i-th row is ai,j (1≤ai,j≤109) — the number written in the j-th cell of the i
# 
# -th row.
# 
# It's guaranteed that the sum of n⋅m
# over all test cases does not exceed 2⋅105
# 
# .
# Output
# 
# If after the swap it is impossible to get a good grid, output −1
# 
# .
# 
# In the other case output 2
# 
# integers — the indices of the columns that should be swapped to get a good grid.
# 
# If there are multiple solutions, print any.

import sys

name = "input"
path = ""

# sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def is_valid(m):
    valid = True
    for i in range(len(m)):
        if valid == False:
            break
 
        for j in range(len(m[0])):
            if j == 0:
                continue
 
            if m[i][j] < m[i][j-1]:
                valid = False
    return valid

for testCase in range(1, testCases + 1):
    rs, cs = list(map(int, input().split(' ')))

    m = []
    cs = [0, 0]
    f = 0

    for i in range(rs):
        a = list(map(int, input().split(' ')))
        sa = sorted(a)

        f = 0
        for idx in range(len(a)):
            if a[idx] != sa[idx]:
                if f > 1:
                    break
                cs[f] = idx
                f += 1

        m.append(a)

        if f > 2:
            break

    if f > 2:
        print(-1)
        continue

    if is_valid(m):
        print("1 1")
        continue

    c1, c2 = cs 

    for i in range(len(m)):
        tmp = m[i][c1]
        m[i][c1] = m[i][c2]
        m[i][c2] = tmp

    if not is_valid(m):
        print(-1)
        continue

    print(c1 + 1, c2 + 1)
