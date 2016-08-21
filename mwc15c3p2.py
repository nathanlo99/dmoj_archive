n, m = map(int, input().split())
k = []
packs = []
for i in range(n):
    k.append(int(input()))
for i in range(m):
    packs.append(list(map(int, input().split()[1:])))
print(k)
print(packs)
