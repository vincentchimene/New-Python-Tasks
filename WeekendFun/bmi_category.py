#QUESTION
#BMI Category : Ask for weight (kg) and height (meters).
#Compute bmi = weight / (height * height) Then print:
#
#< 18.5 → "Underweight"
#between 18.5 and 24.9 → "Normal"
#between 25 and 29.9 → "Overweight"
#>= 30 → "Obese"


#PSEUDOCODE
#collect weight and height
#compute bmi = weight / (height * height)
#compare bmi and return:
#   < 18.5 → "Underweight"
#   between 18.5 and 24.9 → "Normal"
#   between 25 and 29.9 → "Overweight"
#   >= 30 → "Obese"
#call function
#print



def get_bmi(weight, height):
    bmi = weight / (height*height)
    if bmi < 18.5:
        result = "Underweight"
    if bmi >= 18.5 and bmi <= 24.9:
        result = "Normal"
    if bmi >= 25 and bmi <= 29.9:
        result = "Overweight"
    if bmi >= 30:
        result = "Obese"
    return result


weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
print(f"you are {get_bmi(weight, height)}")




        
    
    
    


