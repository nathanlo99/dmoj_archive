def sieve(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

primes = sieve(7010)
def p(n):
    if n < 2:
        return -1
    if n in primes:
        return 1
    if n % 2 == 1:
        if n - 2 in primes:
            return 2
        else:
            return 3
    
    for prime in primes:
        if prime > n // 2:
            return 3
        if n - prime in primes:
            return 2

n, k = map(int, input().split())
if k > 3:
    print(0)
else:
    c = 0
    for i in range(n + 1):
        if p(i) == k:
            c += 1
    print(c)