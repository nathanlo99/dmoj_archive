from math import ceil
a, b, c = map(int, input().split())
print(int(ceil(a / 3.0) + ceil(b / 3.0) + ceil(c / 3.0)))