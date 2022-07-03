"""
ID: justin.59
LANG: PYTHON3
TASK: ride 
"""
import sys

name = "ride"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

am = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def name_to_num(name):
    sum = 1
    for l in list(name):
        sum *= am[l]

    return sum


print(
    "GO"
    if name_to_num(input().lower()) % 47 == name_to_num(input().lower()) % 47
    else "STAY"
)
