"""
ID: justin.59
LANG: PYTHON3
TASK: gift1 
"""
import math
import sys

name = "gift1"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

tc = int(input())

ph = {}
for i in range(tc):
    ph[input()] = 0

while True:
    try:
        g = input()

        a, p = list(map(int, input().split(" ")))

        if p == 0:
            ph[g] += a
            continue

        v = math.floor(a / p)
        lo = a - (v * p)

        ph[g] -= a - lo

        for i in range(p):
            t = input()
            ph[t] += v
    except EOFError:
        break

for g, v in ph.items():
    print(g + " " + str(v))
