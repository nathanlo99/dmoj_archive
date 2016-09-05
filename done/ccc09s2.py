r = int(input())
l = int(input())

rows = []
for row in range(r):
    s = input().split()
    a = 0
    for c in s:
        a *= 2
        if c == "1":
            a += 1
    rows.append(a)

comb = set()
for i in range(r):
    k = ((1 << i) - 1) << (r - 1 - i)
    temp = [x for x in rows]
    for j in range(r - 1):
        if k & (1 << j) != 0:
            temp[j + 1] ^= temp[j]
    comb.add(temp[-1])
print(len(comb))