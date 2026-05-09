number = int(input("Enter a number: "))

for row in range(1, number + 1):
    for _ in range(1, row + 1):
        print("*", end=" ")

    print()