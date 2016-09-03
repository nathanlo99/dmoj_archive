time = int(input())
chores = []
for _ in range(int(input())):
    chores.append(int(input()))
chores.sort()
total = 0
num = 0
for chore in chores:
    if total + chore <= time:
        total += chore
        num += 1
    else:
        break
print(num)