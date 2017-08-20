a, b = int(input()), int(input())
c = 1
while a >= 0 and b >= 0:
    c += 1
    a, b = b, a - b
print(c)