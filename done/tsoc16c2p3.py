import sys, bisect
input = sys.stdin.readline

def prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

a, b, c, d = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    if prime(i):
        lo = (c // i) * i
        if c % i != 0:
            lo += i
        hi = (d // i) * i
        n = (hi - lo) // i + 1
        ans = (ans + (n * (hi + lo)) // 2) % 2016420
print(ans)