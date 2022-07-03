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

name = "auto"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def calc(arr, cur_zero_cost, cur_one_cost=0, left_ptr=0, right_ptr=-1):
    if cur_zero_cost <= cur_one_cost or cur_zero_cost == 0:
        return max(cur_zero_cost, cur_one_cost)

    lv = arr[left_ptr]
    rv = arr[right_ptr]

    if lv < rv:
        if lv == 0:
            return calc(arr, cur_zero_cost - 1, cur_one_cost, left_ptr + 1, right_ptr)
        if lv == 1:
            return calc(arr, cur_zero_cost, cur_one_cost + 1, left_ptr + 1, right_ptr)
    elif rv < lv:
        if rv == 0:
            return calc(arr, cur_zero_cost - 1, cur_one_cost, left_ptr, right_ptr - 1)
        if rv == 1:
            return calc(arr, cur_zero_cost, cur_one_cost + 1, left_ptr, right_ptr - 1)
    elif lv == 1:
        return min(
            calc(arr, cur_zero_cost, cur_one_cost + 1, left_ptr, right_ptr - 1),
            calc(arr, cur_zero_cost, cur_one_cost + 1, left_ptr + 1, right_ptr)
        )
    else:
        return min(
            calc(arr, cur_zero_cost - 1, cur_one_cost, left_ptr, right_ptr - 1),
            calc(arr, cur_zero_cost - 1, cur_one_cost, left_ptr + 1, right_ptr)
        )


for testCase in range(1, testCases + 1):
    arr = list(map(int, list(input())))

    zero_cost = functools.reduce(lambda memo, ii: memo + (1 if ii == 0 else 0), list(arr), 0)

    print(calc(arr, zero_cost))
