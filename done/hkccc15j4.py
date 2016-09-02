import sys
input = sys.stdin.readline

length = int(input())
n = int(input())
segments = []
for i in range(n):
    a, b = map(int, input().split())
    segments.append((a, b))
segments.sort()

stack = [segments[0]]
longest = segments[0][0]
for segment in segments[1:]:
    last_segment = stack[-1]
    if segment[0] <= last_segment[1]:
        stack.pop()
        stack.append((last_segment[0], max(last_segment[1], segment[1])))
    else:
        dist = segment[0] - last_segment[1]
        if dist > longest:
            longest = dist
        stack.append(segment)
dist = length - stack[-1][1]
if dist > longest:
    longest = dist

print(longest)