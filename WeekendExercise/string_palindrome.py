string = input("Enter a word: ")
reverse_string = ""

for character in string:
    reverse_string = character + reverse_string

if reverse_string == string:
    print("It is a palindrome")
else:
    print("It is not a palindrome")