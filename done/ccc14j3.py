m, n = 100, 100

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b: n -= a
    elif a < b: m -= b
print(m)
print(n)
