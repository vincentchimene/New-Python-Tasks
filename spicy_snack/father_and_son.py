#Get the fathers_age
#Get the sons_age
#Calculate the number_of_years as the absolute of (fathers_age - 2 X sons_age)
#Return the number_of_years
#Call the function
#print the return value


def get_number_of_years(fathers_age, sons_age):
    number_of_years = abs(fathers_age - 2 * sons_age)
    return number_of_years



fathers_age = int(input("Enter father's age in years(1-80): ")) 
sons_age = int(input("Enter son's age in years(1-80): "))

if (fathers_age < 1 or fathers_age > 80 or sons_age < 1 or sons_age > 80):
    print("Invalid age entered!")
else:
    print(f"Number of years is {get_number_of_years(fathers_age, sons_age)} years")

