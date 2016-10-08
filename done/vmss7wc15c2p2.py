import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
s2 = ""
for i in range(2 * len(s) + 1):
    s2 += "_" if i % 2 == 0 else s[i // 2]
p = [0 for i in range(len(s2))]
c, r, m, n = 0, 0, 0, 0
for i in range(len(s2)):
    if i > r:
        p[i] = 0
        m = i - 1
        n = i + 1
    else:
        i2 = c * 2 - i
        if p[i2] < r - i:
            p[i] = p[i2]
            m = -1
        else:
            p[i] = r - i
            n = r + 1
            m = i * 2 - n
    while m >= 0 and n < len(s2) and s2[m] == s2[n]:
        p[i] += 1
        m -= 1
        n += 1
    if i + p[i] > r:
        c = i
        r = i + p[i]
ans = 0
c = -1
for i, v in enumerate(p):
    if v > ans:
        ans = v
        c = i
print(s2[c - ans + 1:c + ans:2])
print(ans)