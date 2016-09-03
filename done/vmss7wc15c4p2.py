k = int(input())
s = input()
for i, c in enumerate(s):
    print(chr((ord(c) - ord('A') - 3 * (i + 1) - k + 26) % 26 + ord('A')), end="")