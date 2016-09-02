from itertools import permutations

strings = []
def getStrings(string, length, bits):
    if length == 0:
        if bits == 0:
            strings.append(string)
        return

    if bits > 0:
        getStrings(string + "1", length - 1, bits - 1)
    getStrings(string + "0", length - 1, bits)


for _ in range(int(input())):
    strings = []
    n, k = map(int, input().split())
    getStrings("", n, k)
    print("The bit patterns are")
    for string in strings:
        print(string)
    print()