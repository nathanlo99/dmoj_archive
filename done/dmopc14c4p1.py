in_ = "0123456789ABCDEFGHIJKLMNOP"
out = "9ABCDEFGHIJKLMNOPQRSTUVWXY"

d = {}
for i, o in zip(in_, out):
	d[i] = o

s = input()
for c in s:
	print(d[c], end="")
print()
