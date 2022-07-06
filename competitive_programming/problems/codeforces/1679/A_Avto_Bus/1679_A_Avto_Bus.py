# Spring has come, and the management of the AvtoBus bus fleet has given the order to replace winter tires with summer tires on all buses.
# 
# You own a small bus service business and you have just received an order to replace n
# tires. You know that the bus fleet owns two types of buses: with two axles (these buses have 4 wheels) and with three axles (these buses have 6
# 
# wheels).
# 
# You don't know how many buses of which type the AvtoBus bus fleet owns, so you wonder how many buses the fleet might have. You have to determine the minimum and the maximum number of buses that can be in the fleet if you know that the total number of wheels for all buses is n
# .
 
import sys

name = "input"
path = ""

# sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    w = int(input())

    if w < 4:
        print(-1)
        continue
    
    if w % 2 != 0:
        print(-1)
        continue


    print(
        -(w//-6) or 1,
        (w//4) or 1,
    )

