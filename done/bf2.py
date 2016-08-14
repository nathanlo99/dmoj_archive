s = input()
n = int(input())

t = []
for i in range(len(s) - n + 1):
    t.append(s[i:i + n])
print(t[t.index(sorted(t)[0])])
