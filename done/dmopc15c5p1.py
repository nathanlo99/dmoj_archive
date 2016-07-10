from math import ceil
a = int(input())
b = int(input())
x = int(input())

gcd = lambda a, b: a if b is 0 else gcd(b, a % b)

print(ceil(x * gcd(a, b) / (a * b)))
