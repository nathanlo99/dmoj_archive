s = set(int(input()) for _ in range(int(input())))

for i in range(1, 101):
    n = set(int(100 * k / i + 0.5) for k in range(i + 1))
    if n.issuperset(s):
        print(i)
        break