for _ in range(5):
    c = {}
    n = int(input())
    for i in range(n):
        s = int(input())
        c[s] = c.get(s, 0) + 1
    t = sorted(c.values(), reverse=True)
    if t[0] > n / 2:
        print("verified")
    elif t[0] > t[1]:
        print("unverified")
    else:
        print("unknown")