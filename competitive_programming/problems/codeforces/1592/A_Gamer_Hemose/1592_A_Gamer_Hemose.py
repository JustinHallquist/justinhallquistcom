n = lambda: map(int, input().split())
(tc,) = n()

for _ in range(tc):
    w, h = n()

    m1, m2 = sorted(n())[-2:]

    s = h // (m1 + m2)
    h -= s * (m1 + m2)

    print(2 * s + (2 if h > m2 else 1 if h else 0))
