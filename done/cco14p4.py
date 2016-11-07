import sys
input = sys.stdin.readline

n, p = map(int, input().split())

planets = []
for i in range(1, n + 1):
    a, b = map(int, input().split())
    if i == p:
        s = a
    elif a >= b:
        planets.append((b, a - b))

planets.sort()
num = 1
for b, a in planets:
    if a >= 0 and s >= b:
        num += 1
        s += a

print(s)
print(num)