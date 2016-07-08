s = input()
while s != "0":
    stack = []
    for i in s.split()[::-1]:
        if i in ["*", "/", "+", "-"]:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b + i + " ")
        else:
            stack.append(i + " ")
    print(stack[-1])
    #
    s = input()
