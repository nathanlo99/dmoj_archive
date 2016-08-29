fib = [1, 1]
for i in range(14):
    fib.append(fib[-1] + fib[-2])

n = int(input())
for i, c in enumerate(input()):
    if c == "A" and i + 1 not in fib:
        print("Bruno, GO TO SLEEP")
        break
    if c != "A" and i + 1 in fib:
        print("Bruno, GO TO SLEEP")
        break
else:
    print("That's quite the observation!")