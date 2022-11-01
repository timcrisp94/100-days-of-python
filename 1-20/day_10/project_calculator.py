from art import logo
from os import system, name

# clear function
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')


# add
def add(n1, n2):
  return n1 + n2

# subtract
def subtract(n1, n2):
  return n1 - n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1, n2):
  return n1 / n2 

# operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
def calculator():
  print(logo)
  # num1 input
  num1 = int(input("what's the first number? "))
  calculating = True


  # loop through dictionary, print keys, and ask which operation
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation from the line above: ")

  # num2 input
  num2 = int(input("what's the second number? "))

  # first answer method
  calculation = operations[operation_symbol]
  first_answer = calculation(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")

  # continue calculating
  while calculating:
    continue_calculating = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ")
    if continue_calculating == 'y':
      operation_symbol = input("Pick another operation: ")
      next_num = int(input("What's the next number? "))
      next_answer = calculation(first_answer, next_num)
      print(f"{first_answer} {operation_symbol} {next_num} = {next_answer}")
    else:
      calculating = False
      clear()
      calculator()


calculator()

