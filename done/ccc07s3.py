s = 0
d = {}
f = {}

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a in d:
        a = d[a]
    else:
        d[a] = s
        s += 1
        a = d[a]
    if b in d:
        b = d[b]
    else:
        d[b] = s
        s += 1
        b = d[b]
    f[a] = b

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a not in d or b not in d:
        print("No")
        continue
    a, b = d[a], d[b]
    node = f[a]
    dist = 0
    while node not in [a, b]:
        node = f[node]
        dist += 1
    if node == a:
        print("No")
    else:
        print("Yes", dist)