import sys

a, b, c = map(int, input().split())

for op in "+-*/":
    if eval(str(a) + op + str(b)) == c:
        print(str(a) + str(op) + str(b) + "=" + str(c))
        sys.exit(0)
    if eval(str(b) + op + str(c)) == a:
        print(str(a) + "=" + str(b) + str(op) + str(c))
        sys.exit(0)