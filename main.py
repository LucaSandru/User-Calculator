from os import system, name
from art import logo
print(logo)
def clear():
    if name == 'nt':
        _ = system('cls')

def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide (a, b):
    return a / b
def calculate(number1, number2, op):
    if op == '+':
        return f"{number1} + {number2} = {add(number1, number2)}"
    elif op == '-':
        return f"{number1} - {number2} = {subtract(number1, number2)}"
    elif op == '*':
        return f"{number1} * {number2} = {multiply(number1, number2)}"
    elif op == '/':
        return f"{number1} / {number2} = {divide(number1, number2)}"
number1 = int(input ("What's the first number? "))
operation = input ("Pick an operation: +, -, *, /: ")
ok = 1
k = 0
new_page = True
while ok == 1:
    if k == 2:
        number1 = int(input("What's the first number? "))
        operation = input("Pick an operation: +, -, *, /: ")
        k = 0
    if k == 0:
        number2 = int(input("What's the next number? "))
        result = calculate(number1, number2, operation)
        if operation == '+':
            current = add(number1, number2)
        elif operation == '-':
            current = subtract(number1, number2)
        elif operation == '*':
            current = multiply(number1, number2)
        elif operation == '/':
            current = divide(number1, number2)
        k += 1
        print(result)
    else:
        question = input(f"Type 'y' to continue calculating with {current}, 'n' to start a new calculation or 'q' to quit: ")
        if question == 'n':
            clear()
            k = 2
        elif question == 'y':
            number1 = result
            operation = input("Pick an operation: +, -, *, /: ")
            k = 0
        else:
            ok = 0



