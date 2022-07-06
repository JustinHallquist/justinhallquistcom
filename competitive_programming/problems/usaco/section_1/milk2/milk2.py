"""
ID: justin.59
LANG: PYTHON3
TASK: milk2 
"""
import sys

name = "milk2"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split(" "))))

a = sorted(a, key=lambda x: x[0])

p = []
res_max = 0
res_min = 0

for start, stop in a:
    v = stop - start
    m = 0

    if len(p):
        pstart, pstop = p

        if pstop >= start:
            v = stop - pstart
            p = [pstart, max(stop, pstop)]
        else:
            v = stop - start
            m = start - pstop
            p = [start, stop]
    else:
        v = stop - start
        p = [start, stop]

    res_max = max(res_max, v)
    res_min = max(res_min, m)

print(res_max, res_min)
