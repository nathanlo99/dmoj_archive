c = []
for _ in range(8):
    c.append(int(input()))
c += c
print(max(sum(c[i:i + 4]) for i in range(8)))
