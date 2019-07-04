def composite(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 1
    return 0

cnt = 0
for _ in range(int(input())):
    if composite(int(input())):
        cnt += 1
print(cnt)