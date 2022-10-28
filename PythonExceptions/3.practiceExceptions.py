import math

def rootCalculator(num):
    if num<0:
        raise ValueError("the number cant be negative") #personalize the error
    else:
        return math.sqrt(num)

op1=int(input("type your number: "))
try:
    print(rootCalculator(op1))
except ValueError as negativeNumberError:#catch the error and print your personalize error
    print(negativeNumberError)

print("end of the program")