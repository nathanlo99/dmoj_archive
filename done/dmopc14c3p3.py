import sys
input = sys.stdin.readline

n = int(input())
vets = []
for i in xrange(n):
    name, skill = input().split()
    vets.append((name, int(skill)))
for i in xrange(int(input())):
    a, d = map(int, input().split())
    min_dist = 10000
    min_name = ""
    for name, skill in vets:
        if a <= skill <= a + d:
            if skill - a < min_dist:
                min_name = name
                min_dist = skill - a
    if min_name == "":
        print("No suitable teacher!")
    else:
        print(min_name)