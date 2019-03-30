# Patrick Guha psg486


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponentiate(x, y):
    return x ** y


loop = 1

while loop == 1:

    # user input
    operator = input("Enter operation: ")

    # this immediately lets users go back to the beginning to input a correct operator
    if operator != '+' and operator != '-' and operator != '*' and \
            operator != '/' and operator != '^' and operator != 'q':
        print("Invalid operator, try again")
        continue

    if operator == 'q':
        loop = 0  # just this by itself makes user type in numbers even though they want to quit
        break  # this allows user to quit without having to type in useless numbers

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print(add(num1, num2))

    elif operator == '-':
        print(subtract(num1, num2))

    elif operator == '*':
        print(multiply(num1, num2))

    elif operator == '/':
        print(divide(num1, num2))

    elif operator == '^':
        print(exponentiate(num1, num2))
