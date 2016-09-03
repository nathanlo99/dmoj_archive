import sys
input = sys.stdin.readline

n, m = map(int, input().split())
root = [i for i in range(n + 1)]

def find(n):
    if root[n] != n:
        root[n] = find(root[n])
    return root[n]

def union(x, y):
    xr = find(x)
    yr = find(y)
    if xr != yr:
        root[xr] = yr
    
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

x, y = map(int, input().split())
print(1 if find(x) == find(y) else 0)