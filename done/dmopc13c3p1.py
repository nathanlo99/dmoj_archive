import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for _ in range(m):
    a, b = map(int, input().split())
    t = input()
    d[b] = d.get(b, []) + [t]
me = int(input())
if me in d:
    print("\n".join(d[me]))
