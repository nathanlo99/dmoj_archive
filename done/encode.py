n = 26 - int(input())
for c in input():
    o = ord(c)
    if c == " ":
        print(" ", end="")
    elif o >= ord("a"):
        print(chr(ord("a") + (o - ord("a") + n) % 26), end="")
    else:
        print(chr(ord("A") + (o - ord("A") + n) % 26), end="")
print()