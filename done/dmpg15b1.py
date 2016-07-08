for _ in range(int(input())):
    n = input()
    if len(n) != 10 or n[:3] not in ["416", "647"]:
        print("not a phone number")
    else:
        print("(" + n[:3] + ")-" + n[3:6] + "-" + n[6:])
