num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Enter an operation: +,-,*,/: ")
if operation=="+":
    sum=num1+num2
    print(f"The sum of {num1} and {num2} is: {sum}")
elif operation=="-":
    subtraction=num1-num2
    print(f"The difference of {num1} and {num2} is: {subtraction}")
elif operation=="*":
    multiplication=num1*num2
    print(f"The multiplication of {num1} and {num2} is: {multiplication}")
elif operation=="/":
    division=num1/num2
    print(f"The division of {num1} and {num2} is: {division}")
    