p = lambda: list(map(int, input().split()))
(tc,) = p()

for _ in range(tc):
    n = p()[0]

    a = []
    m = n // 2
    i = 1
    h = set(range(1, n + 1))

    while i <= n:
        a.append(i)
        h.discard(i)

        if i * 2 <= n:
            i *= 2
        else:
            j = n + 1

            for e in h:
                j = e
                break

            if j * 2 > n:
                i = n + 1
            else:
                i = j

    a += h

    print(2)
    print(" ".join(map(str, a)))
