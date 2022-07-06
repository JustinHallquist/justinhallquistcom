"""
ID: justin.59
LANG: PYTHON3
TASK: namenum 
"""
import sys

name = "namenum"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

k = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y"],
}

d = {}
with open("dict.txt") as file:
    for line in file:
        d[line.rstrip()] = 1

n = list(map(int, list(input())))

c = list(map(lambda x: k[x], n))

res = []


def product(*args):
    result = [[]]
    for pool in args:
        result = ["".join(x) + y for x in result for y in pool]

    return result


res = []
for r in product(*c):
    res.append(r)

res2 = []
for b in res:
    if b in d:
        res2.append(b)

if not len(res2):
    print("NONE")
else:
    for b in sorted(res2):
        print(b)
