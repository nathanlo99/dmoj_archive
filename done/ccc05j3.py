directions = [input()]
roads = [input()]

while roads[-1] != "SCHOOL":
	directions.append(input().strip())
	roads.append(input().strip())

for direction, road in zip(directions[::-1], roads[:-1][::-1]):
	d = "LEFT" if direction == "R" else "RIGHT"
	print ("Turn " + d + " onto " + road + " street.")

d = "LEFT" if directions[0] == "R" else "RIGHT"
print ("Turn " + d + " into your HOME.")
