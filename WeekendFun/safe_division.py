#Safe Division: Ask for two integers( x, y).
#Print the result of  x / y  if y  != 0. If  y == 0,  print "Cannot divide by zero".



#collect the first_number
#collect the second_number
#return the result of  first_number / second_number if y  != 0. 
#If  y == 0,  return "Error: Cannot divide by zero".
#call function
#print function



def divide_safely(first_number, second_number):
    if second_number != 0:
        return(first_number/second_number)
    else:
        return "Error: Cannot divide by zero"

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print(f"Quotient: {divide_safely(first_number, second_number)}")
