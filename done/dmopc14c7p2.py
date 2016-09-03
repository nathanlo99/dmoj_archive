from sys import exit
input()
n = list(map(int, input().split()))
a = n.index(min(n))
b = n.index(max(n))
if a > b:
    print("unknown")
    exit(0)
sequence = n[a: b + 1]
if sorted(sequence) == sequence:
    print(sequence[-1] - sequence[0])
else:
    print("unknown")