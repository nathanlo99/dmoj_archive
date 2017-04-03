import sys

min_ = 1
max_ = 2000000000

while True:
    guess = min_ + (max_ - min_) // 2
    print(guess)
    sys.stdout.flush()
    response = input().strip()
    if response == "SINKS":
        min_ = guess + 1
    elif response == "FLOATS":
        max_ = guess - 1
    else:
        break