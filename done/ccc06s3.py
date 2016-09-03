def intersects(x1, y1, x2, y2, x3, y3, x4, y4):
# 	# Bounding box check
	max_y = max(y1, y2)
	min_y = min(y1, y2)
	max_x = max(x1, x2)
	min_x = min(x1, x2)
	max_y1 = max(y3, y4)
	min_y1 = min(y3, y4)
	max_x1 = max(x3, x4)
	min_x1 = min(x3, x4)
	if min_y > max_y1 or max_y < min_y1: return False
	if min_x > max_x1 or max_x < min_x1: return False

	# Check if p1 and p2 lie on different sides of p3p4
	#``Check that (p1p2 x p1p3) * (p1p2 x p1p4) <= 0
	p1p2_p1p3 = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
	p1p2_p1p4 = (x2 - x1) * (y4 - y1) - (x4 - x1) * (y2 - y1)
	if p1p2_p1p3 * p1p2_p1p4 > 0: return False

	# Check if p3 and p4 lie on different sides of p1p2
	p3p4_p3p2 = (x4 - x3) * (y2 - y3) - (y4 - y3) * (x2 - x3)
	p3p4_p3p1 = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
	if p3p4_p3p1 * p3p4_p3p2 > 0: return False

	return True

x1, y1, x2, y2 = map(int, input().split())
c = 0
for i in range(int(input())):
	s = list(map(int, input().split()))
	n = s[0]
	s.append(s[1])
	s.append(s[2])
	if any(intersects(x1, y1, x2, y2, s[2 * j + 1], s[2 * j + 2], s[2 * j + 3], s[2 * j + 4]) for j in range(n)):
		c += 1
print(c)