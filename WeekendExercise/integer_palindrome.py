number = int(input("Enter a number: "))
temp_number = number
reverse_number = 0

while temp_number > 0:
    reverse_number = reverse_number * 10 + temp_number % 10
    temp_number //= 10

if reverse_number == number:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
