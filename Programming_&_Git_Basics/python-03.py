# Basic Calculator

num1= int(input("Enter First Number:"))
num2= int(input("Enter Second Number: "))
op= input(str("Enter Operator: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Operator")   