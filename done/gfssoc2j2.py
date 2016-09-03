a, b = 1, 1
for i in range(int(input())):
    if a % 91 == 0:
        print("Fizz Fuzz", end=" ")
    elif a % 7 == 0:
        print("Fizz", end=" ")
    elif a % 13 == 0:
        print("Fuzz", end=" ")
    else:
        print(str(a), end=" ")
    if b % 91 == 0:
        print("Fizz Fuzz")
    elif b % 7 == 0:
        print("Fizz")
    elif b % 13 == 0:
        print("Fuzz")
    else:
        print(str(b))
    a += 1
    b += 2