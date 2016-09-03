from sys import exit
a = input()
b = input()
for c in "abcdefghijklmnopqrstuvwxyz":
    if a.count(c) < b.count(c):
        print("N")
        exit(0)
print("A")