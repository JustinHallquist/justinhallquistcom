# https://codeforces.com/blog/entry/18051
#
# t = SegmentTree([1, 2, 3, 4])
#
# print(t.t)
# print(t.query(3, 4))  # 4
#
# t.modify(2, 4, 5)
# t.push(2, 4)
# t.build(2, 4)
#
# print(t.t)
# print(t.query(0, 3))  # 8

import math


class SegmentTree:
    def __init__(self, arr):
        self.a = arr
        self.t = [0] * len(arr) * 2
        self.n = len(arr)

        self.h = math.ceil(math.log(self.n + 1))
        self.d = [0] * len(arr)

        self._build()

    def _build(self):
        for i in range(self.n):
            self.t[i + self.n] = self.a[i]
        for i in range(self.n)[::-1]:
            self.t[i] = self.t[i << 1] + self.t[i << 1 | 1]

        return self.t

    def calc(self, p, k):
        if self.d[p] == 0:
            self.t[p] = self.t[p << 1] + self.t[p << 1 | 1]
        else:
            self.t[p] = self.d[p] * k

    def apply(self, p, v, k):
        self.t[p] = v * k

        if p < self.n:
            self.d[p] = v

    def build(self, l, r):
        k = 2

        l += self.n
        r += self.n - 1

        while l > 1:
            l = l >> 1
            r = r >> 1
            i = r

            while i >= l:
                self.calc(i, k)
                i -= 1

    def push(self, l, r):
        s = self.h
        k = 1 << (self.h - 1)

        l += self.n
        r += self.n - 1

        while s > 0:
            i = l >> s

            while i <= r >> s:
                if self.d[i] != 0:
                    self.apply(i << 1, self.d[i], k)
                    self.apply(i << 1 | 1, self.d[i], k)
                    self.d[i] = 0

                i += 1

            s -= 1
            k = k >> 1

    def modify(self, l, r, v):
        if v == 0:
            return None

        self.push(l, l + 1)
        self.push(r - 1, r)

        cl = False
        cr = False
        k = 1

        l += self.n
        r += self.n
        while l < r:
            if cl:
                self.calc(l - 1, k)
            if cr:
                self.calc(r, k)
            if l & 1:
                self.apply(l, v, k)
                l += 1
                cl = True
            if r & 1:
                r -= 1
                self.apply(r, v, k)
                cr = True

            l = l >> 1
            r = r >> 1
            k = k << 1

        l -= 1

        while r > 0:
            if cl:
                self.calc(l, k)
            if cr and (cl == False or l != r):
                self.calc(r, k)

            l = l >> 1
            r = r >> 1
            k = k << 1

    # [l, r)
    def query(self, l, r):
        self.push(l, l + 1)
        self.push(r - 1, r)

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
