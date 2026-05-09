vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


letter = input("Enter a letter: ")

if letter in vowels:
    print("Vowel")
elif letter in consonants:
    print("Consonants")
else:
    print("Invalid input")