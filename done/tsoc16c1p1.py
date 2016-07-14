for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("Yes" if b <= a - d <= c else "No")
