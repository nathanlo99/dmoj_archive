print((lambda a, b, c, d: "ignore" if 
    (a == 8 or a == 9)
 and (d == 8 or d == 9)
 and (b == c)

 else "answer"

)(int(input()), int(input()), int(input()), int(input())))