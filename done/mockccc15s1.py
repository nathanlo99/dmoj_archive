p = int(input())
u = int(input())
r1 = int(input())
r2 = int(input())

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def r(a, b):
    g = gcd(a, b)
    return (a / g, b / g)

ratio = r(r1, r2)

ans = set()

for upvotes in range(u):
    for downvotes in range(u - upvotes):
        dupvotes = u - upvotes - downvotes
        if upvotes * 1 + downvotes * -1 + dupvotes * 2 == p:
            if ratio in [r(upvotes, downvotes),
                         r(downvotes, upvotes),
                         r(upvotes, dupvotes),
                         r(dupvotes, upvotes),
                         r(downvotes, dupvotes),
                         r(dupvotes, downvotes)]:
                ans.add((upvotes, downvotes, dupvotes))
print(len(ans))