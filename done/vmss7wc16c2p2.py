import sys
input = sys.stdin.readline

v = [0]
a = 0
for c in input():
    a += (c == "G")
    v.append(a)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(v[b + 1] - v[a])