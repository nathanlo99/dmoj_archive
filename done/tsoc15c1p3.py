# Will simple brute force be enough?
# Complexity: O(N * R) [100 * 100 = 10000]
elevators = []
for i in range(int(input())):
    elevators.append(int(input()))
for i in range(int(input())):
    src, tar = map(int, input().split())
    closest_so_far = -1
    closest_distance = 1001
    for num, elevator in enumerate(elevators):
        distance = abs(elevator - src)
        if distance <= closest_distance:
            closest_distance = distance
            closest_so_far = num
    print(closest_so_far + 1)
    elevators[closest_so_far] = tar