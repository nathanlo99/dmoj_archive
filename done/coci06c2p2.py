n = sorted(map(int, input().split()))
print(" ".join(str(n[ord(c) - ord("A")]) for c in input().strip()))