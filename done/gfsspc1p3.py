n = int(input())
s = input()

last = "X"
diff_count = 0

for c in s:
    if c != last:
        diff_count += 1
        if diff_count > 3:
            print("FIX YOUR BEADS!")
            break
    last = c
else:
    print("Organized")