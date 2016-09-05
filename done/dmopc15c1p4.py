import sys
input = sys.stdin.readline

def sieve(n):
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

n, x = map(int, input().split())

primes = sieve(150000)

c = 0
for p in primes:
    if p > n:
        break
    c += 2 * ((n - p) // x) + 2
    if (n - p) % x == 0:
        c -= 1

print(c)