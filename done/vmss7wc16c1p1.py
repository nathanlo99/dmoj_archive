n = int(input())
while n is not 1:
    d = 0
    if n % 2 == 0:
        d = 2
    elif n % 3 == 0:
        d = 3
    else:
        for i in range(5, int(n ** 0.5) + 1):
            if n % i == 0:
                d = i
                break
            if n % (i + 2) == 0:
                d = i + 2
                break
    if d == 0:
        print(n)
        break
    print(d)
    n //= d
