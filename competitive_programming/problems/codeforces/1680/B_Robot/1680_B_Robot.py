# There is a field divided into n
# rows and m

# columns. Some cells are empty (denoted as E), other cells contain robots (denoted as R).

# You can send a command to all robots at the same time. The command can be of one of the four types:

#     move up;
#     move right;
#     move down;
#     move left. 

# When you send a command, all robots at the same time attempt to take one step in the direction you picked. If a robot tries to move outside the field, it explodes; otherwise, every robot moves to an adjacent cell in the chosen direction.

# You can send as many commands as you want (possibly, zero), in any order. Your goal is to make at least one robot reach the upper left corner of the field. Can you do this without forcing any of the robots to explode?
# Input

# The first line contains one integer t
# (1≤t≤5000) — the number of test cases.

# Each test case starts with a line containing two integers n
# and m (1≤n,m≤5) — the number of rows and the number of columns, respectively. Then n lines follow; each of them contains a string of m

# characters. Each character is either E (empty cell} or R (robot).

# Additional constraint on the input: in each test case, there is at least one robot on the field.
# Output

# If it is possible to make at least one robot reach the upper left corner of the field so that no robot explodes, print YES. Otherwise, print NO.

import sys

name = "input"
path = ""

# sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    n,m = input().split()

    cur_item = None
    res = "Yes"
    for x in range(int(n)):
        for idx, item in enumerate(list(input())):
            if item == 'E':
                continue;

            if cur_item == None:
                cur_item = [x, idx]
                continue

            if idx < cur_item[1]:
                res = "No"
                break

    print(res)
