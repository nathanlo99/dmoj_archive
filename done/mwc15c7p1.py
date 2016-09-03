from sys import exit

n = int(input())
seq = list(map(int, input().split()))

diff = None
ratio = None
arith = False
geo = False

if max(seq) == min(seq):
    print("both")
    exit(0)

for i in range(1, n):
	if diff is not None and seq[i] - seq[i - 1] != diff: break
	diff = seq[i] - seq[i - 1]
else:
	arith = True

for i in range(1, n):
	if ratio is not None and seq[i - 1] * ratio != seq[i]: break
	if seq[i - 1] == 0: break
	ratio = float(seq[i]) / seq[i - 1]
else:
	geo = True

if geo:
	if arith: print("both")
	else: print("geometric")
else:
	if arith: print("arithmetic")
	else: print("random")