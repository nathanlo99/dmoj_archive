import sys
input = sys.stdin.readline
ss = set(2**n for n in range(64))
for _ in range(int(input())):
    print("FT"[int(input()) in ss])