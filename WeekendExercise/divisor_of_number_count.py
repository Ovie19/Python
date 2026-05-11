number = int(input("Enter a number: "))

count = 1
divisor_count = 0
temp_number = number

while temp_number > 0:
    if number % count == 0:
        divisor_count += 1

    count += 1
    temp_number -= 1

print("The number of divisors is", divisor_count)