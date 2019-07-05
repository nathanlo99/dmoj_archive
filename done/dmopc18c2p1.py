x = []
y = []
for _ in range(int(input())):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
print(2 * (max(x) - min(x) + max(y) - min(y)))