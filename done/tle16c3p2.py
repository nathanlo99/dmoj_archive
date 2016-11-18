import sys
from collections import defaultdict
input = sys.stdin.readline

p, n, v, r = map(int, input().split())
planets = defaultdict(set)
coeffs = []
danger = set()

for i in range(p):
    x, y = map(int, input().split())
    planets[x].add(y)

for i in range(n):
    coeffs.append(int(input()))

def f(x):
    global coeff
    return sum(coeffs[n - 1] * x ** (len(coeffs) + 1 - n) for n in range(1, len(coeffs) + 1))

for x in range(1, v):
    # print("f({}) = {}".format(x, f(x)))
    if f(x) in planets[x]:
        danger.add((x, f(x)))

cx, cy = v, f(v)
for x in range(v - r, v + r + 1):
    for y in planets[x]:
        if (cx - x) ** 2 + (cy - y) ** 2 <= r ** 2:
            danger.add((x, y))
print(len(danger))