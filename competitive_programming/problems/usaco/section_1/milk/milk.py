"""
ID: justin.59
LANG: PYTHON3
TASK: milk
"""
import sys

name = "milk"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

u, i = list(map(int, input().split(" ")))

f = []
for n in range(i):
    f.append(list(map(int, input().split(" "))))


f = sorted(f, key=lambda x: x[0])

t = 0
r = 0
for k in f:
    p, a = k
    if r + a >= u:
        t += p * (u - r)
        r += a
        break

    t += p * a
    r += a

print(t)
