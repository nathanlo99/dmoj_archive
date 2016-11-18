import sys
input = sys.stdin.readline

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(2):
    print(" ".join(str(x + 1) for x in sorted(range(n), key = lambda c: p[c][i])))