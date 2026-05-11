"""

Write a python program to read a number from the
command prompt and print a right triangle using "*"
sample input : 5
sample output.
*
**
***
****
*****

"""

number = int(input("Enter number of rows: "))
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print("*", end="")
    print()    
