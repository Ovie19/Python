import random

def get_random_number():
    return random.randint(1, 100)


count = 0
score = 0

while count < 10:
    first_number = get_random_number()
    second_number = get_random_number()

    attempts = 0
    result = -1
    user_response = 0

    while attempts < 2 and user_response != result:
        if first_number > second_number:
            result = first_number - second_number
            user_response = int(input(f"What is {first_number} - {second_number}? "))
        else:
            result = second_number - first_number
            user_response = int(input(f"What is {second_number} - {first_number}? "))

        if user_response == result:
            print("Correct!!!")
            score += 1
        else:
            print("Wrong. Try again")

        attempts += 1

    print()
    count += 1

print(f"You got {score} out of 10.")