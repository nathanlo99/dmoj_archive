from math import ceil
import random
p = int(input())
q = int(input())
w = int(input())

#find N such that (q - p)/w + p = N

if w is 0 and p < q - 0.5: print("DROP THE COURSE")
else:
	for i in range(100):
		if p * 100 - p * w + i * w >= 100 * q - 50:
			print(i)
			break
	else: print("DROP THE COURSE")