import sys
input = sys.stdin.readline

n = int(input())
a = int(input())
done = set()
j = []
for i in range(1, n + 1):
    j.append(input().strip())
for i in range(a):
    size, num = input().split()
    num = int(num) - 1
    if num in done:
        continue
    have_size = j[num]
    if size == "L" and have_size != "L":
        continue
    if size == "M" and have_size == "S":
        continue
    done.add(num)
print(len(done))