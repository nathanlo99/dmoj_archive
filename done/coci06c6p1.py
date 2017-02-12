
count = {}
num = 0
ans = 0
for _ in range(int(input())):
    s = input()
    num += 1
    if count.get(s, 0) * 2 >= num:
        ans += 1
    count[s] = count.get(s, 0) + 1

print(ans)
