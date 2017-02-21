a = []
for i in range(6):
    a.append(int(input()))
b = int(input())
c = int(input())

print("yes" if sum(a) / 6.0 + b >= c else "no")