next_num = int(input())
num_late = 0
not_served = 0
s = input()
while s != "EOF":
    if s == "TAKE":
        next_num += 1
        if next_num == 1000:
            next_num = 1
        num_late += 1
        not_served += 1
    elif s == "SERVE":
        not_served -= 1
    elif s == "CLOSE":
        print("{} {} {}".format(num_late, not_served, next_num))
        num_late = 0
        not_served = 0
    s = input()