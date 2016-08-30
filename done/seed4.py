import sys
input = sys.stdin.readline

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def gcd_xyz(x, y, z):
    k = gcd(gcd(abs(x), abs(y)), abs(z))
    return x // k, y // k, z // k

x, y, z = map(int, input().split())

k = set()
for i in range(int(input())):
    a, b, c = map(int, input().split())
    g = gcd_xyz(a - x, b - y, c - z)
    k.add(g)
print(len(k))