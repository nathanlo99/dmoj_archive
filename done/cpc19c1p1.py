n = int(input())

ans = []
for i in range(1, (n + 1) // 2 + 1):
    ans.append(i)
    other = n + 1 - i
    if i != other:
        ans.append(other)
print(" ".join(map(str, ans)))