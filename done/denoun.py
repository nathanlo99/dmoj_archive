for _ in range(int(input())):
    c = 0
    for word in input().split():
        if word[0].isupper():
            c += 1
    print(c)