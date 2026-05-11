#Write a program that print even numbers between 1 - 100 in a straight line.

for number in range(1,101):
    if number % 2 == 0:
        print(number, end=" ")
print()
