day, num = map(int, input().split())
day -= 1

print("Sun Mon Tue Wed Thr Fri Sat")
for i in range(day):
    print("    ", end="")
for i in range(1, num + 1):
    print("{:3}".format(i), end=" ")
    if (i + day) % 7 == 0:
        print()