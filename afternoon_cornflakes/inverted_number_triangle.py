"""

Print the following pattern
54321
4321
321
21
1

"""

number = int(input("Enter number of rows: "))
for row in range(number, 0, -1):
    for column in range(row, 0, -1):
        print(column, end="")
    print()    
