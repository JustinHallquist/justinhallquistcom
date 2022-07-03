"""
ID: justin.59
LANG: PYTHON3
TASK: barn1 
"""
import sys

name = "barn1"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

m, s, c = list(map(int, input().strip().split(" ")))

f = []
for n in range(c):
    f.append(int(input().strip()))


f = sorted(f)
g = []

for i, v in enumerate(f):
    if i == 0:
        g.append([0, i])
        continue

    g.append([v - f[i - 1], i])

if m == 1:
    print(f[-1] - f[0] + 1)
elif m >= c:
    print(c)
else:
    g = sorted(sorted(g, reverse=True)[: m - 1], key=lambda x: x[1])

    r = 0
    z = 0
    for v in g:
        _, i = v
        r += f[i - 1] - f[z]
        z = i

    r += f[-1] - f[g[-1][1]]

    print(r + m)
