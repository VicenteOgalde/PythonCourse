userName=input("type your name")
check=False
while check==False: #while for using a try and except for get the age input right
    try:
        userAge=int(input("type your age: "))
        check=True
    except Exception:
        print("type a number please")
print("the user name is: ",userName.upper())#change the string to uppercase
ageUser=""
ageUser=str(userAge)#change the int to str
print(ageUser.isdigit())#checking if the string is a digit