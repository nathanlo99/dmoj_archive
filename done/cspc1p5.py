from math import floor

n = int(input())
courses = []
course_mark = {}
for i in range(n):
    name, mark = input().split()
    mark = int(mark[:-1])
    courses.append((mark, i, name))
    course_mark[name] = mark
courses.sort()
to_drop = input()
should_drop = courses[0][2]
after_optimal_drop = sum(x[0] for x in courses[1:]) / (float(n) - 1)
after_drop = (sum(x[0] for x in courses) - course_mark[to_drop]) / (float(n) - 1)
print("{:.2f}%".format(sum(x[0] for x in courses) / float(n)))
print("{:.2f}%".format(after_drop))
print(should_drop)
print("{:.2f}%".format(after_optimal_drop))
if after_optimal_drop < 95:
    print("You are {}% away from your goal.".format(int(floor(95 - after_optimal_drop))))
else:
    print("You have reached your goal.")