a = int(input())
b = int(input())

print("The number of RSA numbers between", a, "and", b, "is", sum(1 for i in range(a, b + 1) if sum(1 for x in range(1, i+1) if i % x == 0) == 4))
