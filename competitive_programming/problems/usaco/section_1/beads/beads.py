"""
ID: justin.59
LANG: PYTHON3
TASK: beads 
"""
import sys

name = "beads"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

n = int(input())
rb = list(input())
b = rb + rb

bm = {}
tmp = {}

pb = None
ci = 0
w = 0

for idx, v in enumerate(b):
    if v == "w":
        w += 1

    if pb != v and v != "w":
        ci += 1
        bm[ci] = (w * "w") + v

        if ci - 1 in bm:
            bm[ci - 1] += w * "w"

        w = 0
    elif v != "w":
        if ci in bm:
            bm[ci] += (w * "w") + v
        else:
            bm[ci] = (w * "w") + v
        w = 0

    if v != "w":
        pb = v

res = 0

for idx, v in bm.items():
    l = 0
    r = 0

    if idx - 1 in bm:
        l = len(bm[idx]) + len(bm[idx - 1])

        if bm[idx][0] == bm[idx - 1][-1] == "w":
            l -= 1

    if idx + 1 in bm:
        r = len(bm[idx]) + len(bm[idx + 1])
        if bm[idx][-1] == bm[idx + 1][0] == "w":
            r -= 1

    res = max(res, l, r)

if res > len(rb):
    res = len(rb)

print(res or len(rb))
