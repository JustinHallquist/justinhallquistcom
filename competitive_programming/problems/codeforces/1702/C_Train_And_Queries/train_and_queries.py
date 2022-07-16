import sys
from collections import defaultdict


p = lambda: list(map(int, input().split()))
(tc,) = p()
for _ in range(tc):
    p()
    len, qc = p()
    a = input().split()

    m = defaultdict(int)
    m2 = defaultdict(int)

    for i in range(len):
        if m.get(a[i], -1) == -1:
            m[a[i]] = i

        m2[a[i]] = i

    for _ in range(qc):
        s, e = input().split()

        l = m.get(s, -1)
        r = m2.get(e, -1)

        if l != -1 and r != -1 and l < r:
            print("Yes")
        else:
            print("No")
