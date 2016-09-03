n, x = map(int, input().split())
ages = []
wishes = []
c = 0
for i in range(n):
    a, b = map(int, input().split())
    ages.append(a)
    wishes.append(b)
for i, (age, wish) in enumerate(zip(ages, wishes)):
    if i + 1 == n:
        continue
    next_age = ages[i + 1]
    next_wish = wishes[i + 1]
    if age > next_age and wish is 1 and next_wish is 0:
        ages[i], ages[i + 1] = ages[i + 1], ages[i]
    if next_age > age and next_wish is 1 and wish is 0:
        ages[i], ages[i + 1] = ages[i + 1], ages[i]
for age, wish in zip(ages, wishes):
    if age > x and wish is 0:
        c += 1
    if age <= x and wish is 1:
        c += 1
print(c)