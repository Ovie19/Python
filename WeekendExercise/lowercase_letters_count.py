string = input("Enter any word: ")
lowercase_letters_count = 0

for character in string:
    if character == character.lower():
        lowercase_letters_count += 1

print(f"The count of lowercase letters in {string} is {lowercase_letters_count}")