number = 1
counter = 0
while True:
    if number % 3 == 0:
        print(number, end=" ")
        counter = counter + 1
    number = number + 1
    if counter == 15:
        break
print()
