def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

a, m = map(int, input().split())
g, x, y = egcd(a, m)
print(x % m)