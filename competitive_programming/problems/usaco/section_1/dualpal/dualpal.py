"""
ID: justin.59
LANG: PYTHON3
TASK: dualpal 
"""
import math
import sys

name = "dualpal"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

n, s = list(map(int, input().split()))


def convert_base(n, b):
    if n == 0:
        return [0]

    a = []

    while n > 0:
        a.append(int(n % b))
        n //= b

    return int("".join(list(map(str, a[::-1]))))


def is_palendrome(n):
    n = list(str(n))

    s = 0
    e = len(n) - 1
    r = True

    for m in range(math.ceil(len(n) / 2)):
        if n[s] != n[e]:
            r = False
            break
        s += 1
        e -= 1

    return r


t = 0
i = s + 1

while t < n:
    c = 0

    for b in range(2, 11):
        if c > 1:
            break

        a = convert_base(i, b)

        if is_palendrome(a):
            c += 1

    if c > 1:
        print(i)
        t += 1

    if t > n - 1:
        break

    i += 1
