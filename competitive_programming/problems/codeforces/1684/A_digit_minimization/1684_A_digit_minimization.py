# There is an integer n
# 
# without zeros in its decimal representation. Alice and Bob are playing a game with this integer. Alice starts first. They play the game in turns.
# 
# On her turn, Alice must swap any two digits of the integer that are on different positions. Bob on his turn always removes the last digit of the integer. The game ends when there is only one digit left.
# 
# You have to find the smallest integer Alice can get in the end, if she plays optimally.
# Input
# 
# The input consists of multiple test cases. The first line contains a single integer t
# (1≤t≤104
# 
# ) — the number of test cases. Description of the test cases follows.
# 
# The first and the only line of each test case contains the integer n
# (10≤n≤109) — the integer for the game. n
# 
# does not have zeros in its decimal representation.
# Output
# 
# For each test case output a single integer — the smallest integer Alice can get in the end of the game.

import sys

name = "input"
path = ""

# sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    arr = list(map(int, list(input())))

    if len(arr) == 1:
        print(arr[0])
        continue

    if len(arr) == 2:
        print(arr[1])
        continue

    print(min(arr))
