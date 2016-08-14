h = int(input())
for i in range(1, int(input())):
    if -6 * i ** 4 + h * i ** 3 + 2 * i ** 2 + i <= 0:
        print("The balloon first touches ground at hour: \n" + str(i))
        break
else:
    print("The balloon does not touch ground in the given time.")
