# https://www.codewars.com/kata/5c80b55e95eba7650dc671ea

import math
from random import randrange


def complete_binary_tree(arr):
    depth = math.floor(math.log(len(arr), 2))
    root_node = 2**depth- 1
    tree = [None] * (len(arr))
    tree.append(root_node)


    for i in range(depth):
       c=2**i 
       a = [None] * c
       for m in range(c):

           
           
    print(tree)

    return arr


# assert complete_binary_tree([1]) == [1]
# assert complete_binary_tree([1, 2, 3, 4, 5, 6]) == [4, 2, 6, 1, 3, 5]
assert complete_binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
    7,
    4,
    9,
    2,
    6,
    8,
    10,
    1,
    3,
    5,
]

# a = [randrange(10) for i in range(10)]
# assert complete_binary_tree(a) == [a[i] for i in [6, 3, 8, 1, 5, 7, 9, 0, 2, 4]]


1 2 3 4 5 6 7 8 9 10
7 2**n-1  n = log(10,2) = 4
4 2**n-1  n = log(7,2) = 3
