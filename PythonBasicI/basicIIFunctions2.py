#Parameters and arguments are declared inside the parentheses().
#If your function is prepared to receive 2 parameters, you must send them 2 parameters.
#parameters are stored in order, first in first parameter second in second parameter, etc
#you can use return to return the value obtained in a function and you can even save it in a variable

def sum(a,b):
    print(a+b)

sum(5,9)
sum(8,10)
sum(15,101)

def sum_return(a,b):
    return a+b
return_of_sum=sum_return(15,15)
print(return_of_sum)