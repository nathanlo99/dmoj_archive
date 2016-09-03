n = int(input())
m = int(input())
d = [0 for i in range(n + 1)]
for i in range(int(input())):
    a, b, c = map(int, input().split())
    d[a - 1] += c
    d[b] -= c
z = 0
ans = 0
for i in range(n):
    z += d[i]
    if z < m:
        ans += 1
print(ans)