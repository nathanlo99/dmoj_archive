from sys import exit

n = int(input())
a = input()
b = input()
a += a
if b not in a:
    print("-1")
    exit(0)
index = a.index(b)
if index <= n // 2:
    print("L{}".format(index))
else:
    print("R{}".format(n - index))