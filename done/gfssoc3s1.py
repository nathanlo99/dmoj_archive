n = int(input())
count = 0
while n >= (1 << count):
    count += 1
print("1" * count)