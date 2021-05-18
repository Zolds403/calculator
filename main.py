from art import logo

#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

"""This is the end of the functions that are needed"""

operators = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("Whats the first number?: "))
  for symbol in operators:
    print(symbol)
  should_continue = True

  while should_continue:
    operators_symbol = input("Pick an operation: ")
    num2 = float(input("Whats the second number?: "))
    calculation_function = operators[operators_symbol]
    answer = calculation_function(num1, num2)


    print(f"{num1} {operators_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()    

#operators_symbol = input("Pick another operation: ")
#num3 = int(input("Whats the next number?: "))
#calculation_function = operators[operators_symbol]
#second_answer = calculation_function(calculation_function(num1, num2), num3)

#print(f"{first_answer} {operators_symbol} {num3} = {second_answer}")