input()
s = [int(x) for x in input().split()]
a = s[0]
b = s[1:]
for i in b:
    j = a
    for n in range(2, min(i, j) + 1):
        while i % n == 0 and j % n == 0:
            i, j = i // n, j // n
    print("{}/{}".format(j, i))