primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def is_prime(n):
    if n <= 100:
        return n in primes_under_100
    if n % 2 == 0 or n % 3 == 0:
        return False

    for f in range(5, int(n ** .5), 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False
    return True

n = int(input())
while not is_prime(n):
	n += 1
print(n)