string = input("Enter any word: ")
uppercase_letters_count = 0

for character in string:
    if character == character.upper():
        uppercase_letters_count += 1

print(f"The count of uppercase letters in {string} is {uppercase_letters_count}")