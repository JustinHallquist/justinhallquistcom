import sys
from random import randint, random, randrange

name = "input"
path = ""

sys.stdout = open(path + name + ".out", "w")

arr_len = 199927
queries = 199924
maxv = int(1e9)

print(str(arr_len) + " " + str(queries))
print(" ".join([str(randrange(maxv)) for _ in range(arr_len)]))

for i in range(queries):
    k = randint(0, 1)

    if k:
        u = randint(1, arr_len)
        v = randint(1, maxv)
        print("1 " + str(u) + " " + str(v))
    else:
        v = randint(1, maxv)
        print("2 " + str(v))
