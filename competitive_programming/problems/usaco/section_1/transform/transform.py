"""
ID: justin.59
LANG: PYTHON3
TASK: transform
"""
import sys

name = "transform"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")


def rotate90(m):
    l = len(m)
    n = []

    for r in range(l):
        n.append([None] * l)

    i = 0
    while i < l:
        j = 0
        while j < l:
            n[j][l - i - 1] = m[i][j]

            j += 1

        i += 1
    return n


def invert(m):
    l = len(m)
    n = []

    for r in range(l):
        n.append([None] * l)

    i = 0
    while i < l:
        j = 0
        while j < l:
            n[i][l - j - 1] = m[i][j]

            j += 1

        i += 1
    return n


n = int(input())

m1 = []
m2 = []

for i in range(n):
    m1.append(list(input()))

for i in range(n):
    m2.append(list(input()))

res = []

if m1 == m2:
    res.append(6)
elif invert(m1) == m2:
    res.append(4)

r = m1
r2 = m1
for i in range(3):
    r = rotate90(r)
    if r == m2:
        res.append(i + 1)
        break

    if invert(r) == m2:
        res.append(5)
        break

if len(res):
    print(min(res))
else:
    print(7)
