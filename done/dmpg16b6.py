for i in range(int(input())):
    code, number = input().split()
    if code == "A":
        ans = 0
        for c in number:
            ans *= -2
            ans += int(c)
        print(ans)
    else:
        neg = 0 if number[0] == "-" else 1
        ans = [int(x) for x in "{0:b}".format(abs(int(number)))][::-1]
        for i, c in enumerate(ans):
            if i % 2 == neg and c == 1:
                if i + 1 >= len(ans):
                    ans.append(1)
                else:
                    ans[i + 1] += 1
            elif c == 2:
                ans[i] = 0
                if i + 1 >= len(ans):
                    ans.append(1)
                else:
                    ans[i + 1] += 1
        print("".join(map(str, ans[::-1])))