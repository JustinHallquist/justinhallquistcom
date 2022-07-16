import sys
import functools

from collections import defaultdict


name = "input"
path = "/home/jhallquist/git/justinhallquistcom/competitive_programming/problems/codeforces/1692/E_Binary_Dequeue/"

sys.stdin = open(path + name + ".in")


def count(a, v):
    return functools.reduce(lambda memo, _v: memo + (1 if _v == v else 0), list(a), 0)


p = lambda: list(map(int, input().split()))
(tc,) = p()

for _ in range(tc):
    l, v = p()
    a = p()

    zc = count(a, 0)
    oc = count(a, 1)

    if oc < v:
        print(-1)
        continue
    elif oc == v:
        print(0)
        continue
