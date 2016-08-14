maps = {}
first = input()
second = input()
old = input()

for i in range(len(first)):
    maps[second[i]] = first[i]

print("".join((maps.get(x, ".") for x in old)))
