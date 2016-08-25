n = int(input())
gold = [-1, 0, 0, 0, 0]
for _ in range(n):
    s = input()
    for i, c in enumerate(s):
        if c == "g":
            if i < n:
                gold[2] += 1
            else:
                gold[1] += 1
for _ in range(n):
    s = input()
    for i, c in enumerate(s):
        if c == "g":
            if i < n:
                gold[3] += 1
            else:
                gold[4] += 1
gold = sorted(((amt, 6 - num) for num, amt in enumerate(gold)), reverse=True)
print(6 - gold[0][1])