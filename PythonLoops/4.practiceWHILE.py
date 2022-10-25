# code for get a correct age from the user using a while loop
age=int(input("type your age: "))

while age<5 or age>100: #execute while this condition is false
    print("error age, type again ")
    age=int(input("type your real age: "))
print("correct age :"+str(age))