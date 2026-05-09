#    collect number from the user

#    save it in a reference called first_number

#    collect number from the user

#    save it in a reference called second_number

#    collect operator from the user

#    save it in a reference called operator

#    if operator is +, calculate result = addition of first_number and second_number

#        print result

#    if operator is -, calculate result = subtraction of first_number and second_number

#        print result

#    if operator is *, calculate result = multiplication of first_number and second_number

#        print result

#    if operator is /, calculate result = division of first_number and second_number

#        print result

#    else print invalid operator

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("(+, -, *, or /) Enter operator: ")

if operator == "+":
    result = first_number + second_number
    print(f"{first_number} {operator} {second_number} = {result}")

elif operator == "-":
    result = first_number - second_number
    print(f"{first_number} {operator} {second_number} = {result}")

elif operator == "*":
    result = first_number * second_number
    print(f"{first_number} {operator} {second_number} = {result}")

elif operator == "/":
    result = first_number / second_number
    print(f"{first_number} {operator} {second_number} = {result}")

else:
    print("Invalid operator")
