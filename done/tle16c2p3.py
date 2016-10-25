import sys
input = sys.stdin.readline

primes = [True] * 1000000
for i in xrange(3, 1001, 2):
    if primes[i]:
        primes[i * i::2 * i] = [False] * ((1000000 - i * i - 1) // (2 * i) + 1)
primes = [2] + [i for i in xrange(3, 1000000, 2) if primes[i]]

n, c = map(int, input().split())
cut_primes = set()
for i in xrange(c):
    t = int(input())
    pi = 0
    for prime in primes:
        if prime > t:
            break
        while t % prime == 0:
            t //= prime
            cut_primes.add(prime)

for i in xrange(n):
    t = int(input())
    pi = 0
    for prime in cut_primes:
        while t % prime == 0:
            t //= prime
    if t != 1:
        print("N")
        break
else:
    print("Y")