n = int(input())
a = input().split()
b = input().split()

sa, sb = 0, 0
for x, y in zip(a, b):
    if x == y:
        continue
    if x == "rock" and y == "scissors":
        sa += 1
    elif x == "paper" and y == "rock":
        sa += 1
    elif x == "scissors" and y == "paper":
        sa += 1
    else:
        sb += 1
print("{} {}".format(sa, sb))