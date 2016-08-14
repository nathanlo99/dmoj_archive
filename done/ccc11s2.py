d = []
for _ in range(int(input())):
    d.append(input())
c = 0
for _ in range(len(d)):
    if input() == d[_]:
        c += 1
print(c)
