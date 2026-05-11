vowels = ['a', 'e', 'i', 'o', 'u']

position = 0
string = input("Enter any word: ")

for character in string:
    if character in vowels:
        break

    position += 1

print(f"The position of the first vowel in {string} is {position}")