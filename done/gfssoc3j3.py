p = int(input())
t = int(input())
presents = []
teachers = []
for i in range(p):
    name = input()
    price = float(input())
    presents.append((price, name))
for i in range(t):
    name = input()
    mark = int(input())
    teachers.append((mark, name))
for teacher, present in zip(sorted(teachers), sorted(presents)):
    print("{} will get a {}".format(teacher[1], present[1]))