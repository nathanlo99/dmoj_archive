from sys import exit
s = input()

def pal(s):
    return s == s[::-1]

n = len(s)
for i in range(n - 1):
    if s[i] == s[i+1]:
        print("Even")
        break
else:
    print("Odd")