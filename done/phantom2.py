import bisect
import sys
input = sys.stdin.readline

def sieve(n):
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

primes = sieve(1000000)

for _ in xrange(int(input())):
    a, b = map(int, input().split())
    ai = bisect.bisect_left(primes, a)
    bi = bisect.bisect_left(primes, b)
    print(bi - ai)