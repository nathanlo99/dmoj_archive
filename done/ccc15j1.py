a = int(input())
b = int(input())

if a == 2:
	if b > 18:
		print("After")
	elif b < 18:
		print("Before")
	else:
		print("Special")
elif a > 2:
	print("After")
else:
	print("Before")