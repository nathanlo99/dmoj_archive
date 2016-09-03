sx, sy, tx, ty = map(int, input().split())

n = int(input())
d = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if (a * sx + b * sy + c) * (a * tx + b * ty + c) < 0:
        d += 1

print(d)