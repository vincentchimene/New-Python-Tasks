#Ticket Price Calculator: Ask for age.
#Under 5 → “Free"
#5–12 → "$5"
#13–64 → "$12"
#65 or older → "$8" Print the price.


#PSEUDOCODE
#collect age
#compare age assign price:
#    if  5–12 price = "$5"
#        13–64 price = "$12"
#        65 or older price = "$8"
#return price
#call function 
#print return value of function



def get_ticket_price(age):
    if age < 5:
        price = 0
    if age >= 5 and age <= 12:
        price = 5
    if age >= 13 and age <= 64:
        price = 12
    if age >= 65:
        price = 8
    return price


age = int(input("Enter age: "))
print(f"Your ticket price is ${get_ticket_price(age)}")

    

