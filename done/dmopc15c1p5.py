import sys
input = sys.stdin.readline

w, h, n = map(int, input().split())
num = [[0 for i in xrange(w + 1)] for j in xrange(h + 1)]
for i in range(h):
    tmp = map(int, input().split())
    for j, v in enumerate(tmp):
        num[i + 1][j + 1] = v
prefix = [[0 for i in xrange(w + 1)] for j in xrange(h + 1)]
for i in xrange(1, h + 1):
    for j in xrange(1, w + 1):
        prefix[i][j] = num[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

max_ = 0
for sx in xrange(1, min(w, int(n ** 0.5) + 1) + 1):
    sy = n // sx
    if sy > h:
        continue
    for x in xrange(1, w - sx + 2):
        for y in xrange(1, h - sy + 2):
            nx, ny = x + sx - 1, y + sy - 1
            d = prefix[ny][nx] - prefix[y - 1][nx] - prefix[ny][x - 1] + prefix[y - 1][x - 1]
            if d > max_:
                max_ = d
for sy in xrange(1, min(h, int(n ** 0.5)) + 1):
    sx = n // sy
    for x in xrange(1, w - sx + 2):
        for y in xrange(1, h - sy + 2):
            nx, ny = x + sx - 1, y + sy - 1
            d = prefix[ny][nx] - prefix[y - 1][nx] - prefix[ny][x - 1] + prefix[y - 1][x - 1]
            if d > max_:
                max_ = d
print(max_)