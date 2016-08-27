days = int(input())
pages = int(input())
code = input()
num_students = int(input())
perfect_pages = round(pages / float(days))
most_efficient = pages
most_efficient_students = []
for i in range(num_students):
    name, pages, class_code = input().split()
    pages = int(pages)
    if class_code != code:
        continue
    if pages < most_efficient:
        most_efficient = pages
        most_efficient_students = [name]
    elif pages == most_efficient:
        most_efficient_students.append(name)

if len(most_efficient_students) == 1:
    print("The most efficient reader is {}.".format(most_efficient_students[0]))
    if most_efficient == perfect_pages:
        print("This reader is perfectly efficient.")
    else:
        print("None of the readers are perfectly efficient.")
else:
    print("The most efficient readers are {}.".format(",".join(most_efficient_students)))
    if most_efficient == perfect_pages:
        print("These readers are perfectly efficient.")
    else:
        print("None of the readers are perfectly efficient.")