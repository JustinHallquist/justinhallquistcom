"""
ID: justin.59
LANG: PYTHON3
TASK: crypt1 
"""
import math
import sys

name = "crypt1"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

d = int(input().strip())
s = input().strip().split(" ")
n = list(map(int, s))


def product(*args, repeat=1):
    result = [[]]
    pools = [tuple(pool) for pool in args] * repeat
    for pool in pools:
        result = ["".join(x) + y for x in result for y in pool]

    return result


#            a b c     <-- number 'abc'
#          x   d e     <-- number 'de'; the 'x' means 'multiply'
#       -----------
#  p1      * * * *     <-- product of e * abc; first star might be 0 (absent)
#  p2    * * * *       <-- product of d * abc; first star might be 0 (absent)
#       -----------
#        * * * * *     <-- sum of p1 and p2 (e*abc + 10*d*abc) == de*abc

s3 = list(map(int, product(s, repeat=3)))
s4 = list(map(int, product(s, repeat=4)))

r = []
for s in s3:
    for v1 in n:
        r1 = v1 * s

        if r1 not in s3:
            continue

        for v2 in n:
            r2 = v2 * 10 * s

            if r2 / 10 not in s3:
                continue

            r.append(r1 + r2)

print(len([x for x in r if x in s4]))
