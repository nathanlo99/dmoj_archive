def count(s, ss):
    ans = len(s)
    last = -1
    for i in range(len(s)):
        if i >= last and s[i:i + len(ss)] == ss:
            ans -= len(ss)
            ans += 1
            last = i + len(ss)
    return ans + len(ss)

s = input()
ans = len(s)
for i in range(len(s)):
    for j in range(len(s)):
        ans = min(ans, count(s, s[i:j]))
print(ans)