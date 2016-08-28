n = int(input())
k = int(input())

remove = n % k
get = (k - n % k) % k

if n < k:
    print(k - n)
else:
    print(min(remove, get))