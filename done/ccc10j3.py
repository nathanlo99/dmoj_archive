import math

var = {"A":0, "B":0}

s = input().split()
while 1:
	if s[0] == "1": var[s[1]] = int(s[2])
	elif s[0] == "2": print(int(var[s[1]]))
	elif s[0] == "3": var[s[1]] = var[s[1]] + var[s[2]]
	elif s[0] == "4": var[s[1]] = var[s[1]] * var[s[2]]
	elif s[0] == "5": var[s[1]] = var[s[1]] - var[s[2]]
	elif s[0] == "6": var[s[1]] = math.copysign(abs(var[s[1]])//abs(var[s[2]]), var[s[1]]//var[s[2]])
	else: break
	s = input().split()
