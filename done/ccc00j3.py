money = int(input())
a = int(input())
b = int(input())
c = int(input())

ans = 0
while True:
    if money > 0:
        money -= 1
        a += 1
        ans += 1
        if a == 35:
            money += 30
            a = 0
    if money > 0:
        money -= 1
        b += 1
        ans += 1
        if b == 100:
            money += 60
            b = 0
    if money > 0:
        money -= 1
        c += 1
        ans += 1
        if c == 10:
            money += 9
            c = 0
    if money <= 0:
        break
print("Martha plays {} times before going broke.".format(ans))