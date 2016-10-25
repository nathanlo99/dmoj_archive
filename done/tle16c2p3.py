import sys
input = sys.stdin.readline


def sieve(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

primes = sieve(1000000)

n, c = map(int, input().split())
cut_primes = set()
for i in range(c):
    t = int(input())
    pi = 0
    for prime in primes:
        if prime > t:
            break
        while t % prime == 0:
            t //= prime
            cut_primes.add(prime)

# print(cut_primes)
for i in range(n):
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