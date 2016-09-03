from collections import defaultdict

n = int(input()) // 2
returns = defaultdict(set)

for _ in range(n):
    returns[input()].add(input())

if len(returns["lob"]) == 0:
    print("Not enough information")
elif returns["lob"] == {"lob"} and "lob" not in returns["backhand"] | returns["forehand"]:
    print("Possible Bruno")
else:
    print("BruNO")