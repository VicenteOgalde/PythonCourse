print("Scholarships program 2022")
school_distance=int(input("enter the distance in kilometers from your home to the school "))
print("distance from school: "+str(school_distance))
siblings=int(input("enter how many siblings you have "))
print("siblings: "+str(siblings))
family_salary=int(input("enter annual family salary "))
print("annual family salary is: "+str(family_salary))
if school_distance >40 and siblings>2 or family_salary <= 20000: #logic operator 'and' 'or' concatenated different comparison 
    print("you have the right to scholarship")
else:
    print("you dont meet the requirements")
