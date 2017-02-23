alphabet = "0123456789abcdefghijklmnopqrstuvwxyz0"

def convert(s, n):
    if n == 1:
        if all(c == "1" for c in s):
            return len(s)
        return -1
    res = 0
    for c in s:
        idx = alphabet.index(c)
        if idx >= n:
            return -1
        res = n * res + alphabet.index(c)
    return res

for _ in range(int(input())):
    a, op, b, __, c = input().split()
    line = ""
    for i in range(1, 37):
        aa = float(convert(a, i))
        bb = float(convert(b, i))
        cc = float(convert(c, i))
        if aa == -1 or bb == -1 or cc == -1:
            continue
        if eval(str(aa) + op + str(bb)) == cc:
            line += alphabet[i]
    print(line if line else "invalid")