import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = [0]
for num in map(int, input().split()):
    p.append(p[-1] + num)
for _ in range(k):
    a, b = map(int, input().split())
    print(p[a - 1] + p[-1] - p[b])