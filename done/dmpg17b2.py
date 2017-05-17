import sys
input = sys.stdin.readline
s = input().strip()
last = s[-1]
a, b = s.split(",")
if (len(b) == 1):
    print(a + last)
else:
    b = b[1].upper() + b[2:-1]
    if len(a) <= 2: 
        a = ""
    else:
        a = a[0].lower() + a[1:]
    if (len(a) != 0):
        print(b + " " + a + last)
    else:
        print(b + last)