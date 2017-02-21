for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    if (a.startswith(b) or a.startswith(c) or b.startswith(c)
        or b.startswith(a) or c.startswith(a) or c.startswith(b)
        or a.endswith(b) or a.endswith(c) or b.endswith(c)
        or b.endswith(a) or c.endswith(a) or c.endswith(b)):

        print("No")
    else:
        print("Yes")