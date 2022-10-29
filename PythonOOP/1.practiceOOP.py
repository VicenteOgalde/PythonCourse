from operator import truediv


class Car(): #with the reserved word class you create your class
    chassisLength=250 #this is an attribute of your class
    chassisWidth=120
    wheels=4
    running=False

    def startCar(self):#A function becomes a method of the class if it is declared inside the class.
        self.running=True
    def state(self):
        if(self.startCar):
            return "The car is running"
        else:
            return "The car is off"

meCar= Car()#to instantiate a class or create an object just use this type of code nameObject=nameClass()

print(meCar.chassisLength)#by using a dot after the object name you can access its attributes and methods
print(meCar.running)
meCar.startCar()
print(meCar.state())




