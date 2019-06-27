a = int(input())
b = int(input())

even = "01" * 50
odd = "10" * 50
for i in range(b):
    print(even[:a] if i % 2 == 0 else odd[:a])