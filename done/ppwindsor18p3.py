rows = [set(x) for x in ["qwertyuiop", "asdfghjkl", "zxcvbnm"]]

cnt = 0
for _ in range(int(input())):
    s = set(input())
    for row in rows:
        if s.issubset(row):
            cnt += 1
            break
print(cnt)