num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Calculator")
print("1. Add")
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")
print("5. Square")

operation = input("Choose operation (1/2/3/4/5): ")

if operation == '1':
  result = num1 + num2
elif operation == '2':
  result = num1 - num2
elif operation == '3':
  result = num1 * num2
elif operation == '4':  
  result = num1 / num2
elif operation == '5':
  result = num1 ** 2
  
print("Result:", result)