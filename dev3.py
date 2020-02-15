# Program to make a simple calculator
# This function adds two numbers

def add(num1, num2):
   return num1 + num2

# This function subtracts two numbers

def subtract(num1, num2):
   return num1 - num2

# This function multiplies two numbers

def multiplnum2(num1, num2):
   return num1 * num2

# This function divides two numbers

def divide(num1, num2):
   return num1 / num2

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiplnum2")
print("4.Divide")

# Take input from the user

choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Using if,else condition to displanum2 based on the choices entered.

if choice == '1':
   print(num1, "+" ,num2, "=" , add(num1,num2))
   
elif choice == '2':
   print(num1, "-" ,num2, "=" , subtract(num1,num2))
   
elif choice == '3':
   print(num1, "*" ,num2, "=" , multiplnum2(num1,num2))
   
elif choice == '4':
   print(num1, "/" ,num2, "=" , divide(num1,num2))
   
else:
   print("Invalid input!!")
