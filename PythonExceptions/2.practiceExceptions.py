def divide():

    try:
        op1=float(input("type your first number: "))
        op2=float(input("type your second number: "))
        print("the result of your division is : "+str(op1/op2))
    except ValueError:
        print("wrong parameter")
    except ZeroDivisionError: #you can use more the one except
        print("you cant divide by zero")
    finally: #you can use finally for execute a line of code even if the program crashes
        print ("end of the function")


divide()