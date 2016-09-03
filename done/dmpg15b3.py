w, h = map(int, input().split())
c = 0
for _ in range(h):
    n = input()
    for k in n:
        if k in [" ", "#"]:
            print(k, end="")
        elif k is "o":
            c += 1
            print(" ", end="")
        elif k is "*":
            print(" ", end="")
    print("")
print("o" * c)
