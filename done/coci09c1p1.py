lst = list(map(int, input().split()))

if lst == list(range(1, 9)):
    print("ascending")
elif lst[::-1] == list(range(1, 9)):
    print("descending")
else:
    print("mixed")