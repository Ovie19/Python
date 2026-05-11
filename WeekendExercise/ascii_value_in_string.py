string = input("Enter any word: ")

for character in string:
    print(f"{character} => {ord(character)}")