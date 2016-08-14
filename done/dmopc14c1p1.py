marks = []
for i in range(int(input())):
    marks.append(int(input()))
marks.sort()
l = len(marks)
if l % 2 == 0:
    s = marks[l // 2 - 1] + marks[l // 2]
    if s % 2 == 0:
        print(s // 2)
    else:
        print(s // 2 + 1)
else:
    print(marks[l // 2])
