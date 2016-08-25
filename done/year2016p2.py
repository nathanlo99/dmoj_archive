n = int(input())

def suffix(n):
    if n % 10 == 1 and n % 100 != 11:
        return "st"
    elif n % 10 == 2 and n % 100 != 12:
        return "nd"
    elif n % 10 == 3 and n % 100 != 13:
        return "rd"
    else:
        return "th"

s = []
for i in range(n):
    s.append(input())
for i in range(1, n + 1):
    print("On the {}{} day of Christmas my true love sent to me:".format(
        i, suffix(i)))
    if i != 1:
        for j in range(i, 1, -1):
            print("{} {}".format(j, s[j - 1]))
        print("and 1 {}".format(s[0]))
    else:
        print("1 {}".format(s[0]))
    print()