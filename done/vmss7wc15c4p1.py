n = int(input())
c = 0
for i in range(-n, n + 1):
    for j in range(-n, n + 1):
        if i * i + j * j <= n * n:
            c += 1
print(c)
