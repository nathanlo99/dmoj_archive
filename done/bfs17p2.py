c = {}
n = int(input())
for s in input().split():
    c[s] = c.get(s, 0) + 1

most = max(c.values())
remaining = n - most

print(min(most, remaining + 1) + remaining)