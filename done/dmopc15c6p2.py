c = 0.0
for i in range(int(input())):
    c += float(input())
    c %= 360.0
print("{:.5f}".format(c % 360.0))
