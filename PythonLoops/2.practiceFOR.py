email=False
flag=0
in_email=input("Type your email")
for i in in_email: #loop through the string checking all the character
    if i=="@" or i==".": #check if one character is @
        flag=flag+1
if flag>=2: # check if the value is true
    print("correct email")
else:
    print("incorrect email")

for x in range(5): #repeats the number of times that is entered in the range
    print("using range in for "+str(x+1))