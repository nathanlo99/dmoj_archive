boxes = []
for i in range(int(input())):
    boxes.append(sorted(list(map(int, input().split()))))
boxes.sort(key=lambda x: x[0] * x[1] * x[2])
flag = False
for i in range(int(input())):
    item = sorted(list(map(int, input().split())))
    for box in boxes:
        if all(item[j] <= box[j] for j in range(3)):
            print(box[0] * box[1] * box[2])
            break
    else:
        print("Item does not fit.")
