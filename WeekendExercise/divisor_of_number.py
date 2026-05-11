number = int(input("Enter a number: "))

count = 1
temp_number = number

while temp_number > 0:
    if number % count == 0:
        print(count)

    count += 1
    temp_number -= 1