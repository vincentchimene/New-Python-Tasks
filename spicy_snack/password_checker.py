#collect password
#compare password length and assign password_strength according to given conditions
#call function
#print function

def check_password(password):
    if len(password) >= 6 and len(password) <= 10:
        password_strength = "medium"
    elif len(password) >= 1 and len(password) < 6: 
        password_strength = "weak"
    elif len(password) > 10:
        password_strength = "strong"
    elif len(password) < 1:
        password_strength = "invalid"
    
    return password_strength


password = input("Enter your password: ")
print(f"Your password is {check_password(password)}!")


