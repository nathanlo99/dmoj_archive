for _ in range(5):
    stack = [x for x in input().split("/") if x]
    for thing in input().split("/"):
        if thing == ".":
            pass
        elif thing == "..":
            if stack: stack.pop()
        else:
            stack.append(thing)
    print("/" + "/".join(stack))