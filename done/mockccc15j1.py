area, other = input().split()
if area not in ["416", "647", "437"] or len(other) != 7:
    print("invalid")
elif area == "416":
    print("valuable")
else:
    print("valueless")
