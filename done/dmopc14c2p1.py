for i in range(int(input())):
    c = 0
    for _ in range(int(input())):
        c += int(input())
    if c:
        print("Day", str(i + 1) + ":", c)
    else:
        print("Weekend")
