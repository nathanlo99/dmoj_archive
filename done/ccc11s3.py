full = [(1, 0), (2, 0), (3, 0), (2, 1)]
detailed = [(1, 1), (2, 2), (3, 1)]

for _ in range(int(input())):
    m, x, y = map(int, input().split())
    m = 5 ** (m - 1)
    while m:
        xy = (x // m, y // m)
        if xy in full:
            print("crystal")
            break
        elif xy in detailed and m >= 5:
            x, y = x % m, y % m
            m //= 5
        else:
            print("empty")
            break