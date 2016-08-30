n = int(input())
f = 1
w = 1

while f <= n:
    f += w
    w += 1
a = f - w + 1
b = f - 1
n = b - a + 1

print(n * (a + b) // 2)