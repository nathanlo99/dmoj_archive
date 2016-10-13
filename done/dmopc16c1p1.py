input()
ans = 0
for i, v in enumerate(map(int, input().split())):
    if v % 2 == i % 2:
        ans += 1
print(ans)