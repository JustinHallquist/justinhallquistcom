"""
ID: justin.59
LANG: PYTHON3
TASK: friday 
"""
import sys

name = "friday"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

dm = [0, 0, 0, 0, 0, 0, 0]
mm = {
    0: 31,
    1: 28,
    2: 31,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
    11: 31,
}


def is_ly(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        return False

    if y % 4 == 0:
        return True

    return False


ys = int(input())
y = 1900
wd = 1

for i in range(ys):
    ly = is_ly(y)

    m = 0
    md = 0

    mm[1] = 29 if ly else 28

    dy = sum(mm.values())

    for j in range(dy):
        dm[wd] += 1 if md == 13 else 0

        if md == (mm[m] - 1):
            m += 1
            md = 0
        else:
            md += 1

        if wd == 6:
            wd = 0
        else:
            wd += 1

    y += 1

print(" ".join(map(str, dm)))
