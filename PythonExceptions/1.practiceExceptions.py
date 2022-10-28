def sum(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:# here try the code
        return a/b
    except ZeroDivisionError: #catch the exception avoiding the crash of the program
        print("can divide by zero")
        return"wrong operation"
while True: #infinite loop for get the right parameters
    try:
        op1=int(input("type the first number: "))
        op2=int(input("type the second number: "))
        break #the break only work if you enter the right parameters
    except ValueError:
        print("wrong parameters")
        print("try again")


operation=input("type the operation you need to do: sum - subtraction - multiply - divide ")
if(operation=="sum"):
    print(sum(op1,op2))
elif(operation=="subtraction"):
    print(subtraction(op1,op2))
elif(operation=="multiply"):
    print(multiply(op1,op2))
elif(operation=="divide"):
    print(divide(op1,op2))
else:
    print("wrong choice")

print("end of the program")
