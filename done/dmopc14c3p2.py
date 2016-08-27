codes = []
WA = 0
for i in range(int(input())):
    code = input()
    if code == "WA":
        WA += 1
    codes.append(code)

WAtoAC = int((3 * WA) // 10)
IRtoAC = 10
IR = 0
for code in codes:
    if code == "AC":
        print("AC")
    elif code == "WA":
        if WAtoAC > 0:
            print("AC")
            WAtoAC -= 1
        else:
            print("WA")
    elif code == "TLE":
        print("WA")
    elif code == "IR":
        if IR < 10:
            print("AC")
        elif IR < 20:
            print("WA")
        else:
            print("IR")
        IR += 1