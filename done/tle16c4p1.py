s = []
for _ in range(int(input())):
    s.append(int(input()))
a = 0
c = 0
for i in sorted(s):
    if i >= a:
        a += i
        c += 1
print(c)