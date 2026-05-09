def check_palindrome_and_prime(number):
    if number < 1:
        return False

    square_root = int(number ** 0.5)

    for index in range(2, square_root + 1):
        if (number % index == 0):
            return False

    reverse_number = 0
    temp_value = number

    while temp_value > 0:
        reverse_number = reverse_number * 10 + temp_value % 10
        temp_value //= 10

    return reverse_number == number