import sys
input = sys.stdin.readline

f, r = map(int, input().split())
p = [[0] for i in range(f)]
for j in range(f):
    for i in map(int, input().split()):
        p[j].append(p[j][-1] + i)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(p[c - 1][b] - p[c - 1][a - 1])