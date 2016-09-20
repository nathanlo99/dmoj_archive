import sys
input = sys.stdin.readline

n, m, a, b = map(int, input().split())
root = list(xrange(n + 1))

def find_root(n):
    while root[n] != n:
        n = root[n]
    return n

for i in xrange(m):
    x, y = map(int, input().split())
    root[find_root(y)] = find_root(x)

print("GO SHAHIR!" if find_root(a) == find_root(b) else "NO SHAHIR!")