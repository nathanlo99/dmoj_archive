print("Y" if all(y >= x for x, y in zip(sorted(list(map(int, input().split()))), sorted(list(map(int, input().split()))))) else "N")
