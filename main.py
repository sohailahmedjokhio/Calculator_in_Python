def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  return x / y


print("Welcome to Calculator App!")

while True:
  print("\n1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Quit")

  choice = input("Enter your choice (1-5): ")
  if choice == '5':
      print("Thank You for using Calculator App!")
      quit()

  num1 = float(input("Enter the first number: \n"))
  num2 = float(input("Enter the second number: \n"))

  if choice == '1':
      result = add(num1, num2)
      operation = '+'

  elif choice == '2':
      result = subtract(num1, num2)
      operation = '-'

  elif choice == '3':
      result = multiply(num1, num2)
      operation = '*'

  elif choice == '4':
      if num2 == 0:
          print("Invalid number! 0 cannot perform this operation.")
          continue
      result = divide(num1, num2)
      operation = '/'

  print(f"{num1} {operation} {num2} = {result}")