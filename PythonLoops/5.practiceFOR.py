phrase="Python is great"
counter=0
for letter in phrase:
    if letter==" ": #if the string have a blank space jump to the next iteration using continue
        continue
    counter=counter+1

print(counter)

email=input("type your email")

for letter in email:
    if letter=="@":
        checkEmail=True
        break #if you find the character '@' you finish the for with a break
    else:
        checkEmail=False
print(checkEmail)
