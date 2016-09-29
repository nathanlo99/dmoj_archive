i = int(input())
if i < 3:
    print([0, 9, 18][i])
elif i > 20:
    print(1000000000 - 2)
elif i % 2 == 0:
    s = "1" + "9" * (i // 2 - 1) + "8"
    print(s[-9:])
else:
    s = "10" + "9" * (i // 2 - 1) + "8"
    print(s[-9:])