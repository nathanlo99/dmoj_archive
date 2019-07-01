memo = {}

def is_prime(m):
    if m <= 1:
        return False
    if m % 2 == 0 and m > 2:
        return False
    if m % 3 == 0 and m > 3:
        return False
    if m not in memo:
        for i in range(2, int(m**0.5) + 1):
            if m % i == 0:
                memo[m] = False
                break
        else:
            memo[m] = True
    return memo[m]

for _ in range(int(input())):
    n = int(input())
    for i in range(2, n):
        if is_prime(i) and is_prime(n + n - i):
            print(i, n + n - i)
            break
    else:
        print("yikes")