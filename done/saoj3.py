import sys

count = {}
letters = "abcdefghijklmnopqrstuvwxyz"

for c in sys.stdin.read():
    count[c] = count.get(c, 0) + 1

print(" ".join(map(str, (count.get(c, 0) + count.get(chr(ord(c) - 32), 0) for c in letters))))