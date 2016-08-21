from sys import exit
num = {}
for i in range(int(input())):
    a = int(input())
    num[a] = num.get(a, 0) + 1
ans = -1
for i in num:
    if num[i] == i and i > ans:
        ans = i
if 0 not in num and ans == -1:
    ans = 0
print(ans if ans != -1 else "Paradox!")
