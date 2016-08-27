general = []
girls = []
teams = []

for i in range(int(input())):
    name, t, points = input().split()
    points = int(points)
    if t == "general":
        general.append((points, name))
    elif t == "girls":
        girls.append((points, name))
        general.append((points, name))

general.sort(reverse=True)
girls.sort(reverse=True)

if len(girls) >= 1:
    teams.append(girls[0][1])
if len(general) >= 1:
    if general[0][1] not in teams:
        teams.append(general[0][1])
    elif len(general) >= 2:
        teams.append(general[1][1])
if len(general) >= 2:
    if general[1][1] not in teams:
        teams.append(general[1][1])
    elif len(general) >= 3:
        teams.append(general[2][1])

if teams == []:
    print("No ECOO :(")
else:
    print("\n".join(sorted(teams)))