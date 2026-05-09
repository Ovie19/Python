#    collect password from the user

#    save it in a reference called password

#    save length of password characters in a reference called password_length

#    if password_length is less than 1 print invalid

#    if password_length is less than 6 print weak

#    if password_length is greater than 6 but less than or equal to 10 print medium

#    if password_length is greater than 10 print strong

password = input("Enter your password: ")
password_length = len(password)

if password_length < 1:
    print("Invalid")

elif password_length < 6:
    print("Weak")

elif password_length <= 10:
    print("Medium")

else:
    print("Strong")