import sys
input = sys.stdin.readline

rows = int(input())
values = list(map(int, input().split()))
n = rows * (rows + 1) // 2
m = []
x = [-1 for _ in xrange(n)]

i = -1
for row in xrange(1, rows + 1):
    for col in xrange(1, row + 1):
        i += 1
        mat_row = [0.0 for _ in xrange(n)]
        p0, p1, p2, p3, p4 = map(float, input().split())
        if p0 != 0.0:
            mat_row[i - row] = -p0
        if p1 != 0.0:
            mat_row[i - row + 1] = -p1
        if p2 != 0.0:
            mat_row[i + row] = -p2
        if p3 != 0.0:
            mat_row[i + row + 1] = -p3
        mat_row[i] = 1.0
        mat_row.append(p4 * values[i])
        m.append(mat_row)

for j in xrange(n):
    for i in xrange(j + 1, n):
        c = m[i][j]/m[j][j]
        for k in xrange(n + 1):
            m[i][k] -= c * m[j][k]

x[n - 1] = m[n - 1][n] / m[n - 1][n - 1]
for i in xrange(n - 1, 0, -1):
    sum_ = 0
    for j in xrange(i + 1, n + 1):
        sum_ += m[i - 1][j - 1] * x[j - 1]
    x[i - 1] = (m[i - 1][n] - sum_) / m[i - 1][i - 1]

print(x[0])