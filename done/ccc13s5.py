n = int(input())

ans = 0
while n > 1:
    f = 2
    while f <= int(n ** 0.5) + 1 and n % f != 0: 
        f += 1 

    if f < n and n % f == 0:
        x = n // f
        n -= x
        ans += n // x
    else:
        n -= 1
        ans += n
print(ans)