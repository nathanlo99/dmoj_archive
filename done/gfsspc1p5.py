n = int(input())
t = int(input())
p = sorted(int(input()) for i in range(n))

ans = 100000
for i in range(n - t + 1):
    a = p[i]
    b = p[i + t - 1]
    d = min(abs(a), abs(b))
    w = d + b - a
    if w < ans:
        ans = w
print(ans)