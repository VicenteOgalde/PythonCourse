president_salary=int(input("type the president salary "))
print("president salary: "+str(president_salary)) #str cast from int to string, for avoid errors
director_salary=int(input("type the director salary "))
print("director salary: "+str(director_salary))
admin_salary=int(input("type the administrator salary "))
print("administrator salary: "+str(admin_salary))

if admin_salary<director_salary<president_salary: #concatenated condition operators
    print("correct data")
else:
    print("incorrect data")
