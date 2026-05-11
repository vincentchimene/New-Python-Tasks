

def checker(user_number):
    user_number = str(user_number)
    is_palindrome = False
    is_prime = True
    number = int(user_number)
    reversed_number = ""
    for digit in user_number:
        reversed_number = digit + reversed_number
    if reversed_number == user_number:
        is_palindrome = True
    for count in range(2, number//2):
        if number % count == 0:
            is_prime = False
            break
    if is_palindrome == True and is_prime == True:
        is_palindrome_and_prime = True
    else:
        is_palindrome_and_prime = False
    return is_palindrome_and_prime



            
    


