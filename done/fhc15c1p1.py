def sieve(n):
    sieve = [0] * (n + 1)
    for i in range(2, n, 2):
        sieve[i] += 1
    for i in range(3, n, 2):
        if sieve[i] == 0:
            for j in range(i, n, i):
                sieve[j] += 1
    return sieve

p = sieve(10000050)
for i in range(1, int(input()) + 1):
    a, b, k = map(int, input().split())
    c = 0
    for j in range(a, b + 1):
        if p[j] == k:
            c += 1
    print("Case #{}: {}".format(i, c))