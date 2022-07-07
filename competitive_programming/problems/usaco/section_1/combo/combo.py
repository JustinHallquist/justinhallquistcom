"""
ID: justin.59
LANG: PYTHON3
TASK: combo 
"""
import sys

name = "combo"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

n = int(input())
x1, y1, z1 = list(map(int, input().strip().split(" ")))
x2, y2, z2 = list(map(int, input().strip().split(" ")))


def mod_n(num):
    return num % n


def combine(x, y, z):
    return str(mod_n(x)) + ", " + str(mod_n(y)) + ", " + str(mod_n(z))


res = set()

# total iter => 2*(5**3)
for i in range(-2, 3):
    for j in range(-2, 3):
        for k in range(-2, 3):
            res.add(combine(x1 + i, y1 + j, z1 + k))
            res.add(combine(x2 + i, y2 + j, z2 + k))

print(len(res))
