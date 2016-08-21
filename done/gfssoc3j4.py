last = None
ans = True
last_fifth_dir = 0 # 1 if fifth up, 0 if no fifth, -1 if fifth down
for i in range(int(input())):
    s = input()
    note = int(s[1]) * 7 + "CDEFGAB".index(s[0])
    if last_fifth_dir != 0:
        if (note - last) * last_fifth_dir > 0 or abs(note - last) >= 4:
            ans = False
    if last is not None:
        if abs(note - last) >= 7:
            ans = False
        if abs(note - last) >= 4:
            last_fifth_dir = 1 if note > last else -1
        else:
            last_fifth_dir = 0
    last = note
    if not ans:
        break

print("Melodious!" if ans else "Salieri's music")
