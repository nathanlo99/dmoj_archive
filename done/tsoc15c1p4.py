from sys import exit

t = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())

if (a + b) % 2 != (c + d) % 2:
    print("Cannot physically get there.")
    exit(0)

e, f = a + b, b - a
g, h = c + d, d - c

j = (abs(h - f) + abs(g - e)) // 2
if j <= t:
    print("It takes {} minute(s) to get to ({}, {}).".format(j, c, d))
else:
    print("Cannot get there on time.")