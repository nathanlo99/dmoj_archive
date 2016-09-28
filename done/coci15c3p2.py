import itertools
a, b = map(int, input().split())

words = []
length = 1
while len(words) < b / 2:
    words += map(lambda x: "".join(x), itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=length))
    length += 1

print(" ".join(words[:b]))