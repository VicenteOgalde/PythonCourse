class Person():
    def __init__(self, name, age, residence):
        self.name=name
        self.age=age
        self.residence=residence

    def description(self):
        print("name: ",self.name,"\nage: ",self.age,"\nresidence: ",self.residence)

class Employee(Person):
    def __init__(self,salary,seniority,nameEmployee,ageEmployee,residenceEmployee):
        super().__init__(nameEmployee,ageEmployee,residenceEmployee)# use super for call the constructor of the class person
        self.salary=salary
        self.seniority=seniority
    def description(self):
        super().description()
        print("Salary: ",self.salary,"\nSeniority: ",self.seniority)
john=Employee(1500,2,"john",25,"spain")
john.description()
print(isinstance(john,Employee))# you can you can check if it is an instance of some class (person, employee,etc)
