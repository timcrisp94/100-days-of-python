from art import logo




# calculator

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

num1 = int(input("what's the first number? "))
num2 = int(input("what's the second number? "))

# loop through dictionary, print keys, and ask what to do
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

# our method
answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

# their method
# calculation_function = operations[operation_symbol]
# answer2 = calculation_function(num1, num2)
# print(f"{num1} {operation_symbol} {num2} = {answer2}")
