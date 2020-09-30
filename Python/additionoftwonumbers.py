# This program adds two numbers
num1 = int(input("Enter your first number :"))
num2 = int(input("Enter your  second number :"))

try:
  if int(num1) and int(num2):
    print(f"Your answer is {num1+num2}.")

  elif float(num1) and float(num2):
    print(f"Your answer is {num1+num2}."  
    
except:
   print("Please check your input")
