for _ in range(int(input())):
    a, b, c = input().split()
    if a == b:
        print(a)
    elif a == c:
        print(a)
    elif b == c:
        print(b)
    else:
        print("???")