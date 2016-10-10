for i in range(int(input())):
    
    max_depth = 0
    depth = 0
    length = int(input())
    messages = [input() for j in range(length)]
    stack = [messages[-1]]
    for s in messages:
        if len(stack) >= 2 and s == stack[-2]:
            stack.pop()
            depth -= 1
        else:
            stack.append(s)
            depth += 1
            max_depth = max(max_depth, depth)
    print(length * 10 - max_depth * 20)