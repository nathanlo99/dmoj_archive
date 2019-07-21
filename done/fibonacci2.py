n = int(input())
mod = 1000000007
a, b = 0, 1

for bit in bin(n)[2:]:
    c = (a * (b * 2 - a)) % mod
    d = (a * a + b * b) % mod
    if bit == "0":
        a, b = (c, d)
    else:
        a, b = (d, c+d)
print(a % mod)