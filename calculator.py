def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error! Division by zero"
    return a/b
def calculator():
    print("Simple Calculator")
    print("The Operations are:+,-,*,/")
    while True:
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            operator=input("Enter the operator to do the calculation:")
            if operator=='+':
                result=add(num1,num2)
            elif operator=='-':
                result=subtract(num1,num2)
            elif operator=='*':
                result=multiplication(num1,num2)
            elif operator=='/':
                result=division(num1,num2)
            else:
                result="Invalid operator!"
            print("Result:",result)
        except ValueError:
            print("Please enter valid numbers.")
        choice=input("Do you want to continue?(y/n):").lower()
        if choice!="y":
            print("Exiting calculator")
            break
calculator()
