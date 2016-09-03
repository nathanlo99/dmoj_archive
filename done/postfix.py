tokens = input().strip().split()
stack = []

for t in tokens:
    if t in ["+", "-", "*", "/", "%", "^"]:
        if t == "^": t = "**"
        a = stack.pop()
        b = stack.pop()
        stack.append(float(eval(str(b) + t + str(a))))
    else:
        stack.append(float(t))

print(stack[-1])