shoes = input().split()
left = []
right = []
for idx, shoe in enumerate(shoes):
    if shoe == "L":
        left.append(idx + 1)
    else:
        right.append(idx + 1)
print(left[0], right[0])
print(left[1], right[1])