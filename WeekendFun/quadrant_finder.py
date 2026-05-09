#Ask for two integers x and y. Print:
#"Q1" if x > 0 and y > 0
#"Q2" if x < 0 and y > 0
#"Q3" if x < 0 and y < 0
#"Q4" if x > 0 and y < 0
#"Origin" if both zero
#"X-axis" if y == 0 and x != 0
#"Y-axis" if x == 0 and y != 0


def get_quadrant(x, y):
    if x > 0 and y > 0:
        result = "Q1"
    elif x < 0 and y > 0:
        result = "Q2"
    elif x < 0 and y < 0:
        result = "Q3"
    elif x > 0 and y < 0:
        result = "Q4"
    elif x != 0 and y == 0:
        result = "X-axis"
    elif x == 0 and y != 0:
        result = "Y-axis"

    return result


x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
print(get_quadrant(x, y))






