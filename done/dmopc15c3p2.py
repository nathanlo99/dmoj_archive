input()
s = list(map(int, input().split()))
total = sum(s)
if total % len(s) != 0:
    print("Impossible")
else:
    average = total / len(s)
    print(int(sum(abs(amt - average) for amt in s) / 2))
