def check_prime(number):
    if number < 1:
        return False

    square_root = int(number ** 0.5)

    for index in range(2, square_root + 1):
        if (number % index == 0):
            return False

    return True

count = 0
for index in range(101):
    is_prime = check_prime(index)
    if is_prime:
        count += 1

print("The count of prime numbers from 1 to 100 is", count)