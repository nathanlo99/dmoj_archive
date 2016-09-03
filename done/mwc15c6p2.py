import sys
input = sys.stdin.readline
from bisect import bisect_left

def sieve(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

primes = sieve(500000)
input()
for c in map(int, input().split()):
    if c <= 2:
        print("no can do")
    else:
        print(primes[bisect_left(primes, c) - 1])