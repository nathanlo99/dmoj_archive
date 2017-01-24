c, n = map(int, input().split())
b = []
r = 0
for i in range(c):
    s = input()
    a = {"TOK": 1, "English": 2, "Chemistry": 3, "Math": 4}[s]
    b.append(a)
    r += a
if r > n:
    print("Go to Metro")
    b.sort()
    c = 0
    for i in b:
        n -= i
        c += 1
        if n < 0:
            break
    print(c - 1)
else:
    print("YEA BOI")