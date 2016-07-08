d = {2:['A','B','C'], 3:['D','E','F'], 4:['G','H','I'], 5:['J','K','L'],
 6:['M','N','O'], 7:['P','Q','R','S'], 8:['T','U','V'], 9:['W','X','Y','Z']}

n = int(input())
for _ in range(n):
	num = input().replace('-', '')[:10]
	for i in num[:]:
		for k, v in d.items():
			if i in v: 
				num = num.replace(i, str(k))
	print(num[:3] + "-" + num[3:6] + "-" + num[6:])
