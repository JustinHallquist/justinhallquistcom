# Once upon a time Mike and Mike decided to come up with an outstanding problem for some stage of ROI (rare olympiad in informatics). One of them came up with a problem prototype but another stole the idea and proposed that problem for another stage of the same olympiad. Since then the first Mike has been waiting for an opportunity to propose the original idea for some other contest... Mike waited until this moment!
#
# You are given an array a
# of n integers. You are also given q
#
# queries of two types:
#
#     Replace i
#
# -th element in the array with integer x
# .
# Replace each element in the array with integer x
#
#     .
#
# After performing each query you have to calculate the sum of all elements in the array.
# Input
#
# The first line contains two integers n
# and q (1≤n,q≤2⋅105
#
# ) — the number of elements in the array and the number of queries, respectively.
#
# The second line contains n
# integers a1,…,an (1≤ai≤109) — elements of the array a
#
# .
#
# Each of the following q
# lines contains a description of the corresponding query. Description begins with integer t (t∈{1,2}
#
# ) which denotes a type of the query:
#
#     If t=1
#
# , then two integers i and x are following (1≤i≤n, 1≤x≤109
# ) — position of replaced element and it's new value.
# If t=2
# , then integer x is following (1≤x≤109
#
#     ) — new value of each element in the array.
#
# Output
#
# Print q
# integers, each on a separate line. In the i-th line print the sum of all elements in the array after performing the first i queries.

import math
import sys

name = "input"
path = ""

sys.stdin = open(path + name + ".in")
# sys.stdout = open(path + name + ".out2", "w")


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


l, qc = list(map(int, input().split()))
s = list(map(int, input().split()))

st = SegmentTree(s)

for i in range(qc):
    q = list(map(int, input().split()))

    if q[0] == 1:
        l = q[1] - 1
        r = q[1]
        v = q[2]
        st.modify(l, r, v)
        print(st.query(0, st.n))
    else:
        l = 0
        r = st.n
        v = q[1]
        st.modify(l, r, v)
        print(v * len(s))
