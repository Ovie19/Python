base = int(input("Enter a number: "))
exponent = int(input("Enter the power: "))

result = 1
for _ in range(exponent):
    result *= base

print(result)