mod = 998244353

def pow(n, p):
    n %= mod
    if p == 0:
        return 1
    if p % 2 == 0:
        return pow(n * n, p // 2)
    return n * pow(n * n, p // 2)
    
n = int(input())
print(pow(2, (n * (n + 1) // 2)) % mod)