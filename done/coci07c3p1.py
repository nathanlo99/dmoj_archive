a, b, c = sorted(list(map(int, input().split())))

if 2 * b == a + c:
    print(c + c - b)
else:
    if c - b > b - a:
        print((b + c) // 2)
    else:
        print((a + b) // 2)