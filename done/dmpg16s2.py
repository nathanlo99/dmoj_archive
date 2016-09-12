n, k, d = map(int, input().split())

ans = 0
for _ in range(d):
    ans += n % k
    n //= k
ans += n
print(ans)