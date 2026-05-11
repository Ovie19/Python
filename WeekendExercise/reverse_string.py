string = input("Enter any word: ")

reverse_string = ""

for character in string:
    reverse_string = character + reverse_string

print(reverse_string)