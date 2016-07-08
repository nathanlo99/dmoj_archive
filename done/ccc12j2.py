import sys

data = []
for _ in range(4):
	data.append(int(input()))
if data[0] > data[1] > data[2] > data[3]:
	print("Fish Diving")
elif data[0] < data[1] < data[2] < data[3]:
	print("Fish Rising")
elif data[0] == data[1] == data[2] == data[3]:
	print("Fish At Constant Depth")
else:
	print("No Fish")
