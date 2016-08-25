for _ in range(int(input())):
    s = input()
    c = 1
    d = {}
    while s is not "":
        line = ""
        for word in s.split():
            if word in d:
                line += "{} ".format(d[word])
            else:
                line += word + " "
                d[word] = c
                c += 1
        print(line)
        try:
            s = input()
        except EOFError:
            break