def xor(n):
    r = n % 4
    if r == 0:
        return n
    elif r == 1:
        return 1
    elif r == 2:
        return n + 1
    else:
        return 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    xor_a = xor(a - 1)
    xor_b = xor(b)
    print(xor_a ^ xor_b)