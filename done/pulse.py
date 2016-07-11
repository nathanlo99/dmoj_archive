n, s, t = map(int, input().split())
c = 0
for i in range(n):
    a = int(input()) * 2
    if s <= a <= t:
        c += 1
print(c)
