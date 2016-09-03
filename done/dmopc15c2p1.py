n = int(input())
k = int(input())

total = n
swords = n
while swords >= k:
    new_swords = swords // k
    swords -= new_swords * k
    total += new_swords
    swords += new_swords
print(total)