s = [float(int(input())) for i in range(int(input()))]

while True:
    op = input().strip()
    if op == "77":
        print(" ".join(str(int(round(stream))) for stream in s))
        break
    elif op == "88":
        num = int(input())
        s = s[:num - 1] + [s[num - 1] + s[num]] + s[num + 1:]
    elif op == "99":
        num = int(input())
        percent = int(input())
        s = s[:num - 1] + [s[num - 1] * (percent / 100.)] + [s[num - 1] * ((100 - percent) / 100.)] + s[num:]