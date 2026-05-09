#Discount Eligibility : Ask for total_bill and is_member ("yes"
#or "no"). Apply discount:
#If total_bill >= 1000 and is_member == "yes" → 10% off
#If total_bill >= 1000 but not member → 5% off
#Else → No discount Print final amount and discount
#message.


def get_discount_elegibility(total_bill, is_member):
    if total_bll >= 1000 and is_member.lower == yes:
        discount = 10
        
    elif total_bll >= 1000 and is_member.lower == no:
        discount = 5
    else:
        discount = 0
    final_amount = total_bill*(1 - discount/100)
    return (final_amount)


total_bill = float(input("Enter your total bill: "))
is_member = input("Are you a member? ")
print(f"Your Total bill is {total_bill}")

