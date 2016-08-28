import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
d = [0 for i in range(n)]
v = [0 for i in range(n)]
for i in range(n):
    d[i] = int(input())
for i in range(n):
    v[i] = max(abs(d[i] - d[i - 1]), abs(d[i] - d[(i + 1) % n]))

ans = 0
for i in range(n):
    if (d[i] >= k) ^ (v[i] <= l):
        ans += 1
print(ans)