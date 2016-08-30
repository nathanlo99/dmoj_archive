import sys
input = sys.stdin.readline

v = [0]
a = 0
for c in input():
    if c == "G":
        a += 1
    v.append(a)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(v[b + 1] - v[a])