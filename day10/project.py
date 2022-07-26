#Calculator 
from art import logo
import os
def add(n1, n2):
    '''Returns the sum of two numbers'''
    return n1 + n2

def subtract(n1, n2):
    '''Subtracts n2 from n1 returns the result'''
    return n1 - n2

def multiply(n1, n2):
    '''Returns the produt of n1 and n2'''
    return n1 * n2

def divide(n1, n2):
    '''Divides n1 by n2 and returns the result'''
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)
num1 = 0
answer = ''
continue_calculating = True
calculating_again_with_previous = False
while continue_calculating:
    if calculating_again_with_previous == False:
        num1  = float(input("What is the first number?: "))
    for operator in operations:
        print(operator)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer} ")
    cal_again = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation or anykey to end program: ")
    if cal_again == 'y':
        calculating_again_with_previous = True
        num1 = answer
    elif cal_again == 'n':
        calculating_again_with_previous = False
        os.system('clear')
        print(logo)
    else:
        continue_calculating = False
        
    
#Solution with recursion

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('clear')
      calculator()

calculator()

    