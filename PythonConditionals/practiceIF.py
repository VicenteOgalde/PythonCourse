print("Evaluation program of students grades")

student_grade=input("Enter your grade: ") #input capture data via console
def evaluation(grade):
    rate=""
    if grade>5: #this is executed only if true
        rate="approved"
    else: #otherwise the following code is executed
        rate="fail"
    return rate #return the value of rate
print(evaluation(int(student_grade))) #call the function and cast student_grade to int for avoid errors

