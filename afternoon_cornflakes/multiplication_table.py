"""
Write a Python program to create the
multiplication table (from 1 to 10) of a given
number

"""
number = int(input("Enter the number: "))
for count in range(1, 11):
    print(f"{number} X {count:<2} = {number*count:<24}")
    
