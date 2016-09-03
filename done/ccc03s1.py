square = 1
trans = {54:19, 90:48, 99:77, 9:34, 40:64, 67:86}
quit = False

while(not quit):
	d = int(input())
	if d == 0: quit = True; break
	if square + d <= 100: square = trans.get(square + d, square + d)
	print("You are now on square", square)
	if square == 100: break
if not quit: print("You Win!")
else: print("You Quit!")