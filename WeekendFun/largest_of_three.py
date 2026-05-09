#Largest of Three: Ask for three integers a, b, c.
#Print the largest one. Use only two if statements
#(no elif, no max()).
#

def get_max(first_number, second_number, third_number):
    max_value = first_number
    if second_number > max_value:
        max_value = second_number
    if third_number > max_value:
        max_value = third_number
    return max_value


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
print(f"The maximum number is {get_max(first_number, second_number, third_number)}")


