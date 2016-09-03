import sys
input = sys.stdin.readline

a = input()
b = input()

def factorial(n):
    ans = 1
    for i in xrange(1, n + 1):
        ans *= i
    return ans
    
d = {}
for c in a: d[c] = d.get(c, 0) - 1
for c in b: d[c] = d.get(c, 0) + 1
d[a] = d.get(a, 0) + 1

ans = factorial(sum(d.values()))
for x in d.values():
    ans //= factorial(x)
print(ans % 1000000007)