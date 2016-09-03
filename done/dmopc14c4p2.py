a = []
for i in range(int(input())):
    a.append(len(input()))
n = [0 for i in range(int(input()))]

for i in a:
    b = n.index(min(n))
    print(b + 1)
    n[b] += i