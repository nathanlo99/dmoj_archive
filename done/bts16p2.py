c = int(input())
t, f = False, False
for _ in range(c):
    s = input()
    if s[0] == "1":
        if s[2] == "t":
            print("false" if t else "true")
            t = True
        else:
            print("false" if f else "true")
            f = True
    elif s[0] == "2":
        if s[2] == "t":
            print("true" if t else "false")
            t = False
        else:
            print("true" if f else "false")
            f = False
    elif s[0] == "3":
        if s[2] == "t":
            print(-1 if not t else (0 if not f else 1))
        else:
            print(-1 if not f else 0)
    else:
        if f:
            print("false", end=" ")
        if t:
            print("true", end=" ")
        print()