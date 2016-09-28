import sys
input = sys.stdin.readline

s = input()
s = s.replace("x", "({x})")

rem, mod = map(int, input().split())
b = eval(s.format(x=0))
m = eval(s.format(x=1)) - b

b, m = b % mod, m % mod

for i in xrange(mod):
    if (m * i + b) % mod == rem:
        print(i)
        break