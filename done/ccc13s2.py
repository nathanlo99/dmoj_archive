weight = int(input())
cars = []
for _ in range(int(input())):
    cars.append(int(input()))
num = 0
while num < len(cars):
    if sum(cars[max(0, num - 3):num + 1]) > weight: break
    else: num += 1
print(num)
