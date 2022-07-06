import math


class SegmentTree:
    def __init__(self, arr):
        self.a = arr
        self.t = [0] * len(arr) * 2
        self.n = len(arr)

        self.h = math.log(self.n + 1) - 1
        self.d = [0] * len(arr)

        self.build()

        for i, v in enumerate(arr):
            self.t = self.modify(i, v)

    def apply(self, p, v):
        self.t[p] += v

        if p < self.n:
            self.d[p] += v

    def build(self):
        for i in range(self.n)[::-1]:
            self.t[i] = self.t[i << 1] + self.t[i << 1 | 1]

        return self.t

    def modify(self, p, v):
        p += self.n
        self.t[p] = v

        while p > 1:
            self.t[p >> 1] = self.t[p] + self.t[p ^ 1]
            p = p >> 1

        return self.t

    # [l, r)
    def query(self, l, r):
        res = 0

        l += self.n
        r += self.n

        while l < r:
            if l & 1:
                res += self.t[l]
                l += 1

            if r & 1:
                r -= 1
                res += self.t[r]

            l = l >> 1
            r = r >> 1

        return res


t = SegmentTree([1, 2, 3, 4])
print(t.t)
print(t.query(0, 2))
print(t.modify(0, 6))
print(t.query(0, 2))
