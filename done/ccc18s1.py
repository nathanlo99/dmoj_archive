s = []
for i in range(int(input())):
    s.append(int(input()))
s.sort()

ans = 100000000000000
for i in range(len(s) - 2):
    a = s[i]
    c = s[i + 2]
    ans = min(ans, c - a)
print("%.1f" % (ans / 2.0))