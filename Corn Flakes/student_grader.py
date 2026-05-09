count = 0
fail_count = 0
pass_count = 0

while count < 15:
    score = int(input("Enter student score: "))
    if score >= 45:
        pass_count += 1
    else:
        fail_count += 1

    count += 1

print(f"\nFailed: {fail_count}")
print(f"Passed: {pass_count}")