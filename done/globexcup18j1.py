n = int(input())
up = 0
for i in range(n):
    if float(input()) % 1 >= 0.5:
        up += 1
print(up)
print(n - up)