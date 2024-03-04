# Task 1
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

print(f'Hi {name} {surname}, your age are {age}')

# Task 2
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit  - 32) * 5/9

print("Temperature in Fahrenheit:", celsius)

# Task 3
score = float(input("Enter your score: "))

if score >= 90:
    grade = "5"
elif score >= 80:
    grade = "4"
elif score >= 70:
    grade = "3"
elif score >= 60:
    grade = "2"
else:
    grade = "1"

print("Your grade is:", grade)

# Task 4
number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))

if number1 % number2 == 0:
    result = "Devidet"
else:
    result = "Not devidet"

print("The numbers is:", result)

# Task 5
var_int = int(input("Enter an integer value: "))
var_float = float(input("Enter a float value: "))
var_str = input("Enter a string value: ")
var_bool = input("Enter a boolean value (True or False): ").lower() == "true"

type_int = type(var_int).__name__
type_float = type(var_float).__name__
type_str = type(var_str).__name__
type_bool = type(var_bool).__name__

print("Type of var_int:", type_int)
print("Type of var_float:", type_float)
print("Type of var_str:", type_str)
print("Type of var_bool:", type_bool)

# Task 6
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 or side1 + side3 > side2 or side3 + side2 > side1:
    triangle_type = "Can be"
else:
    triangle_type = "Can not be"

print("The triangle is:", triangle_type)

# Task 7
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
  if num2 != 0:
    result = num1 / num2
  else:
    print("Can not devide by 0")
else:
    result = "Invalid operation"

print("Result:", result)