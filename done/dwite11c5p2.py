for _ in range(5):
    c = 0
    n = int(input())
    for i in range(1, n + 1):
        for d in range(1, i + 1):
            if i % d == 0 and (i / d) >= d:
                c += 1
    print(c)