s = input()
n = len(s)

best = s
for i in range(1, n):
    for j in range(i+1, n):
        new = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if new < best:
            best = new
print(best)