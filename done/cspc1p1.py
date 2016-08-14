too_young = 0
able = 0
for i in range(int(input())):
    d = int(input())
    if d < 0:
        continue
    if d < 14:
        too_young += 1
    elif d >= 14:
        able += 1

if too_young == 1:
    print("1 person is too young to play.")
elif too_young != 0:
    print("{} people are too young to play.".format(too_young))

if able < 12:
    print("There are not enough people to play.")
elif able > 12:
    print("There are too many people who want to play.")
else:
    print("Time to play!")
