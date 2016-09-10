d = {"1": "1", "8": "8", "6": "9", "9": "6", "0": "0"}

a = int(input())
b = int(input())
ans = 0
for i in range(a, b + 1):
    s = str(i)
    l , r = 0, len(s) - 1
    while l <= r:
        if s[l] not in d or s[r] not in d:
            break
        if d[s[l]] != s[r]:
            break
        l += 1
        r -= 1
    else:
        ans += 1
print(ans)