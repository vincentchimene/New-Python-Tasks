#collect first_number
#collect operator
#collect second_number
#compare operator and compute result based on operator collected
#return result
#call function 
#print result


def calculate(first_number, operator, second_number):
    match operator:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
        case "/":
            result = first_number / second_number

    return result



first_number = int(input("Enter first number: "))
operator = input("Enter operator: ")
second_number = int(input("Enter second number: "))

print(f"Result: {calculate(first_number, operator, second_number)}")
