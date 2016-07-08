motels = [ 0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000 ]
a = int(input())
b = int(input())
for i in range(int(input())):
	motels.append(int(input()))
motels.sort()

trips = [1]
for i in range(1, len(motels)):
	count = 0
	n = 1
	while i - n >= 0:
		d = motels[i] - motels[i - n]
		if d >= a and d <= b:
			count += trips[i - n]
		n += 1
	trips.append(count)
print(trips[-1])
