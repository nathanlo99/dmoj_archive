n = int(input())
mem = []

while len(mem) < n:
    mem += list(input().split())

if mem[0] + mem[1] == "4D5A":
    ptr = int(mem[0x3C + 0], 16) << 0 | int(mem[0x3C + 1], 16) << 4 | int(mem[0x3C + 2], 16) << 8 | int(mem[0x3C + 3], 16) << 12
    if ptr < 0 or ptr > n + 1:
        print("MZ")
    else:
        name = mem[ptr] + mem[ptr + 1]
        if name == "4E45":
            print("NE")
        elif name == "4C45":
            print("LE")
        elif name == "5045":
            print("PE")
        elif name == "4D5A":
            print("MZ")
        else:
            print("NE")
else:
    print("COM")