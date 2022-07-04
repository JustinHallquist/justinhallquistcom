# You are given three positive integers a, b, c (a<b<c). You have to find three positive integers x, y, z
# 
# such that:
# 
# xmody=a,
# ymodz=b,
# zmodx=c.
# 
# Here pmodq
# denotes the remainder from dividing p by q
# 
# . It is possible to show that for such constraints the answer always exists.
# Input
# 
# The input consists of multiple test cases. The first line contains a single integer t
# (1≤t≤10000
# 
# ) — the number of test cases. Description of the test cases follows.
# 
# Each test case contains a single line with three integers a
# , b, c (1≤a<b<c≤108
# 
# ).
# Output
# 
# For each test case output three positive integers x
# , y, z (1≤x,y,z≤1018) such that xmody=a, ymodz=b, zmodx=c
# 
# .
# 
# You can output any correct answer.

import sys

name = "input"
path = ""

# sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    a, b, c = list(map(int, input().split(' ')))

    # a < b < C
    #
    # x = a + b + c
    # y = b + c
    # z = c

    # x = (a + b + c) % (b + c)
    # y = (b + c) % (c)
    # z = (c) % (a + b + c)

    print(a + b + c, b + c, c)
