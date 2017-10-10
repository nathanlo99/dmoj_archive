import sys
input = sys.stdin.readline

s = list(ord(c) - ord("a") for c in input().strip()[::-1])
ans = []

for i, n in enumerate(s):
    ans.append(0)
    if 0 <= n <= 12:
        ans += s[i + 1:]
        break
    elif i == len(s) - 1:
        ans.append(0)
        break
    elif s[i + 1] != 25:
        s[i + 1] += 1
        ans += s[i + 1:]
        break
    else:
        continue

print("".join(chr(ord("a") + n) for n in ans[::-1]))