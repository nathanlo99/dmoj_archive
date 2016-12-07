n = int(input())
a = set()
for i in range(n):
    s = tuple(sorted(map(int, input().split())))
    a.add(s)
if len(a) == n:
    print("No two snowflakes are alike.")
else:
    print("Twin snowflakes found.")