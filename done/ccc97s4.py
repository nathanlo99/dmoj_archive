n = int(input())
for _ in range(n):
    d = {}
    c = 1
    while True:
        try:
            s = input()
        except EOFError:
            break
        if s == "":
            break
        words = s.split()
        for word in words:
            if word in d:
                print(d[word], end=" ")
            else:
                print(word, end= " ")
                d[word] = c
                c += 1
        print()
    print()