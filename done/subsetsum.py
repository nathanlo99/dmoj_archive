import random
N=25
A=[random.randint(-1000000000, 1000000000) for i in xrange(N)]
print N
print "\n".join(map(str, A))
random.shuffle(A)
S=sum(A[:4])
print S