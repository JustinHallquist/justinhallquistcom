"""
ID: justin.59
LANG: PYTHON3
TASK: palsquare 
"""
import math
import sys

name = "palsquare"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

b = int(input())

s = "0123456789ABCDEFGHIJKLMNOP"


def convert_base(n, b):
    if n == 0:
        return [0]

    a = []

    while n > 0:
        a.append(int(n % b))
        n //= b

    return "".join([s[x] for x in a[::-1]])


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


for n in range(1, 301):
    a = convert_base(n, b)
    c = convert_base(n**2, b)
    if is_palendrome(c):
        print(a, c)
