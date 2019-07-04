s = input()

on = False
buffer = ""
for c in s:
    if c == ":":
        if on:
            print(buffer)
            buffer = ""
            on = False
        else:
            on = True
    else:
        if on:
            buffer += c