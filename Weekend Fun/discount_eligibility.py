total_bill = float(input("Enter total bill: "))
is_member = input("Are you a member (yes or no)? ")

discount = 0
discount_message = ""

if total_bill >= 1000 and is_member.lower() == "yes":
    discount = 10
    discount_message = "10% off"

elif total_bill >= 1000 and is_member.lower() != "yes":
    discount = 5
    discount_message = "5% off"
else:
    discount_message = "No discount"

final_price = total_bill - (total_bill * discount / 100)

print()
print(discount_message, f"Final price: {final_price}", sep="\n")