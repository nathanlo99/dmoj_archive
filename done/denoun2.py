import sys
input = sys.stdin.readline

for _ in range(int(input())):
    for i in input().decode("utf-8").split():
        if i[0].isupper():
            print(i.rstrip('?:!.,;').encode("utf-8"))