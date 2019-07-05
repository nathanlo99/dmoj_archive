r1, g1, b1 = map(int, input().split())
r2, g2, b2 = map(int, input().split())

print("Dull" if int(r1**0.5) == int(r2**0.5) and int(g1**0.5) == int(g2**0.5) and int(b1**0.5) == int(b2**0.5) else "Colourful")