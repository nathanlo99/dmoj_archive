people = []
for _ in range(int(input())):
    name, div, tech, comp, robotics, total = input().split()
    total = int(total)
    robotics = float(robotics)
    t_rob = (robotics * total) / 100
    people.append((t_rob, div, name))

print("These Team Members Should Be Cut:")
for div in ["Design", "Electrical", "Programming", "Business", "Strategy"]:
    print("{}:".format(div))
    s = 0
    n = 0
    team = []
    for person in people:
        if person[1] == div:
            s += person[0]
            n += 1
            team.append(person)

    if n != 0:
        average = s / n
        for person in team:
            if person[0] < average:
                print(person[2])
    print()