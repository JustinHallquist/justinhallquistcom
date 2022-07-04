import sys
import random 
 
testCases = int(input())

with open('auto.in', 'a') as file:
    file.write(f"{testCases}\n")

    for x in range(testCases):
        if x % (testCases / 100) == 0:
            print(x)
        _str = ''.join(random.choice('01') for _ in range(random.randint(1, 50)))
        file.write(f"{_str}\n")
