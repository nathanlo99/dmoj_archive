x = int(input())
i = 2
while i * i < x:
    t = []
    n = x
    while n:
        t.append(n % i)
        n //= i
    if t[::-1] == t:
        print(i)
    i += 1

while i > 0:
    if (x - i) % i == 0 and (x - i) // i > i:
        print((x - i) // i)
    i -= 1