lit = []

c = 0
n = int(input())
m = int(input())
k = int(input())
for i in range(m):
    t = int(input())
    for dt in range(-k, k+1):
        lit.append(t + dt)
for i in range(1, n + 1):
    if i not in lit:
        c += 1
        for dt in range(0, 2 * k+1):
            lit.append(i + dt)
print(c)