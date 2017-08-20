for _ in range(int(input())):
    m, x, y = map(int, input().split())
    m = 5 ** (m - 1)
    while m:
        xy = (x // m, y // m)
        if xy in ((1, 0), (2, 0), (3, 0), (2, 1)):
            print("crystal")
            break
        elif xy in ((1, 1), (2, 2), (3, 1)) and m >= 5:
            x, y, m = x % m, y % m, m // 5
        else:
            print("empty")
            break