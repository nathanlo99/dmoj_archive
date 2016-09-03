input()
first = input().split()
second = input().split()
partners = {}
for index, name in enumerate(first):
    partners[name] = second[index]

flag = True
for person in partners:
    if partners[person] == person:
        flag = False
        break
    if partners[partners[person]] != person:
        flag = False
        break
print("good" if flag else "bad")