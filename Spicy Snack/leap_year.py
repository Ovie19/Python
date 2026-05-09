#   collect year from the user through the terminal

#   save the year in a reference called year

#   check if the year is divisible by 4

#   check if the year is not divisible by 100

#   check if it is divisible by 400

year = int(input("Enter the year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")