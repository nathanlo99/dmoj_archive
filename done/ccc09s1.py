from math import ceil, floor

a = int(input())
b = int(input())

if a == b:
    print(1)
else:
    print(floor(pow(b, 1/6)) - ceil(pow(a, 1/6)) + 1)
