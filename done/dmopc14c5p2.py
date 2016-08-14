m = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if m == None or b - a > m:
        m = b - a
print(m)
