n, m, k = map(int, input().split())

def bitcount(x):
    return 0 if x == 0 else (x%2) + bitcount(x//2)
    
blue = bitcount((n ^ m) & ((1 << k) - 1))
print(blue, k - blue)