n = int(input())
bases = []
names = []
for i in range(n):
    name, base = input().split()
    names.append(name)
    bases.append(int(base))

for i in range(int(input())):
    for j in range(n):
        change = int(input().split()[-1])
        bases[j] += change

p = int(input())
t = sorted(zip(bases, names), reverse=True)
print(t[p - 1][1])