import sys
input = sys.stdin.readline

n = int(input())
half = (n + 1) // 2
s = [input() for _ in range(n)]
hori = True
vert = True
di_a = True
di_b = True

h = {".": ".", "O": "O", "(": ")", ")": "(", "\\": "/", "/": "\\"}
v = {".": ".", "O": "O", "(": "(", ")": ")", "\\": "/", "/": "\\"}
d = {".": ".", "O": "O", "(": "", ")": "", "/": "/", "\\": "\\"}
for i in range(half):
    for j in range(half):
        if s[i][j] not in h[s[i][n - 1 - j]]:
            hori = False
        if s[i][j] not in v[s[n - 1 - i][j]]:
            vert = False

for i in range(n):
    for j in range(j, n):
        if s[i][j] not in d[s[j][i]]:
            di_a = False

for i in range(n):
    for j in range(i + 1):
        if s[i][j] not in d[s[n - 1 - j][n - 1 - i]]:
            di_b = False

ans = 0
if hori:
    ans += 1
if vert:
    ans += 1
if di_a:
    ans += 1
if di_b:
    ans += 1
print(ans)