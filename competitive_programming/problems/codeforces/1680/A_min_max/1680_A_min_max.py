# An array is beautiful if both of the following two conditions meet:
# 
#     there are at least l1
# 
# And at most r1
# Elements in the array equal to its minimum;
# There are at least l2
# And at most r2
# 
#     elements in the array equal to its maximum. 
# 
# For example, the array [2,3,2,4,4,3,2]
# Has 3 elements equal to its minimum (1-st, 3-rd and 7-th) and 2 elements equal to its maximum (4-th and 5
# 
# -th).
# 
# Another example: the array [42,42,42]
# Has 3 elements equal to its minimum and 3
# 
# Elements equal to its maximum.
# 
# Your task is to calculate the minimum possible number of elements in a beautiful array.
# Input
# 
# The first line contains one integer t
# (1≤t≤5000
# 
# ) — the number of test cases.
# 
# Each test case consists of one line containing four integers l1
# , r1, l2 and r2 (1≤l1≤r1≤50; 1≤l2≤r2≤50
# 
# ).
# Output
# 
# For each test case, print one integer — the minimum possible number of elements in a beautiful array.array

import sys

name = "input"
path = ""

# sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    l1, r1, l2, r2 = map(int, input().split())

    res = max(l1, l2)

    if l2 >= l1 and l2 <= r1:
        print(res)
        continue

    if l1 >= l2 and l1 <= r2:
        print(res)
        continue

    print(res + min(l1, l2))
    

