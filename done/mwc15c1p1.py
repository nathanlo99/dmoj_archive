n = int(input())

songs = []
for _ in range(n):
	m, s = map(int, input().split())
	songs.append(m * 60 + s)

m, s = map(int, input().split())
total = m * 60 + s

songs.sort()

for i in range(n):
	total -= songs[i]
	if total < 0:
		print(i)
		break
else:
	print(n)
