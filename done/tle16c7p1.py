import sys
input = sys.stdin.readline

for _ in xrange(int(input())):
    s = input()[4:]
    if 'x' not in s:
        print("y' = 0")
        continue
    a = 1
    x = s.index('x')
    if x != 0:
        if s[:x] == '-':
            a = -1
        else:
            a = int(s[:x])
    if '^' not in s:
        print("y' = " + str(a))
        continue
    hat = s.index('^')
    b = int(s[hat + 1:])
    aa = a * b
    bb = b - 1
    if aa == 0:
        print("y' = 0")
        continue
    elif bb == 0:
        print("y' = " + str(aa))
    elif bb == 1:
        print("y' = " + str(aa) + "x")
    elif aa == 1:
        if bb == 1:
            print("y' = x")
        else:
            print("y' = x^" + str(bb))
    elif aa == -1:
        if bb == 1:
            print("y' = -x")
        else:
            print("y' = -x^" + str(bb))
    else:
        print("y' = " + str(aa) + "x^" + str(bb))