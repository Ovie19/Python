first_term = 0
second_term = 1

count = 2
print(first_term, second_term, end=" ")
while count < 20:
    new_term = first_term + second_term
    first_term = second_term
    second_term = new_term
    print(second_term, end= " ")
    count += 1

print()