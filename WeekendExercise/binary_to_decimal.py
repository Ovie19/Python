binary_number = input("Enter a binary number: ")

count = len(binary_number) - 1
decimal_number = 0

for character in binary_number:
    decimal_number += int(character) * 2 ** count
    count -= 1

print(f"The decimal number of {binary_number} is {decimal_number}")