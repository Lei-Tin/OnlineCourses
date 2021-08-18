from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h > 0 and h < 9:
        break

counter = 0

for i in range(h):
    counter += 1
    for j in range(h - 1):
        print(" ", end="")
    for k in range(counter):
        print("#", end="")

    print("  ", end="")

    for l in range(counter):
        print("#", end="")

    print()
    h -= 1
