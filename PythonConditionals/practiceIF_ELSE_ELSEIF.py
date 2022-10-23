print("Access verification")
user_age=int(input("type your age: ")) #cast the input to int
if user_age <18:
    print("not allowed to enter")
elif user_age>100:  #elif is like else if on JAVA concatenates a new condition
    print("wrong age")
else:
    print("allow to enter")
print("The program is finish")