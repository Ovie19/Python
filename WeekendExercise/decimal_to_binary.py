decimal_number = int(input("Enter a number: "))

binary_number = ""

while decimal_number > 0:
    digit = decimal_number % 2
    binary_number = str(digit) + binary_number
    decimal_number //= 2

print(f"The binary number is {binary_number}")
