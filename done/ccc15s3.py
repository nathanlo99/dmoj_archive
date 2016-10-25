import sys
input = sys.stdin.readline

root = [0 for i in range(100001)]

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
    
n = int(input())
p = int(input())
for i in range(1, n + 1):
    root[i] = i
    
i = 0
while i < p:
    g = int(input())
    temp = find(g)
    if temp == 0:
        print(i)
        break
    root[find(temp)] = find(temp - 1)
    i += 1
else:
    print(p)