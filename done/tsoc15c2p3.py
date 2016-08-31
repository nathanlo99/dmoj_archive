a = input()
b = input()

def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans
    
d = {}
for c in a: d[c] = d.get(c, 0) - 1
for c in b: d[c] = d.get(c, 0) + 1
d[a] = d.get(a, 0) + 1

count = sum(d.values())
ans = factorial(count)
for x in d.values():
    ans //= factorial(x)
print(ans % 1000000007)