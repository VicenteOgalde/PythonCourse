class Car(): #with the reserved word class you create your class
    def __init__(self): #this is the constructor of your class, it contains the parameters with which the object of this will be created using the reserved word __init__
        self.__chassisLength=250 #this is an attribute of your class
        self.__chassisWidth=120 #using __attributeName you can encapsulate this attribute, to make it inaccessible from outside the class
        self.__wheels=4
        self.__running=False

    def startCar(self, starting):#A function becomes a method of the class if it is declared inside the class.
        self.__running=starting
        if(self.__running):
            check=self.__internalChecking()
        if(self.__running and check):
            return "The car is running"
        elif(self.__running and check==False):
            return "something wrong with the check"
        else:
            return "The car is off"
    def state(self):
        print("the car have "+str(self.__wheels)+" wheels , chassis length of "+str(self.__chassisLength)+" and chassis width of "+str(self.__chassisWidth)+".")
    def __internalChecking(self):#using __functionName you can encapsulate this method, to make it inaccessible from outside the class
        print("checking...")
        self.gas="ok"
        self.oil="ok"
        self.doors="closed"
        if self.gas=="ok" and self.oil=="ok" and self.doors=="closed":
            return True
        else:
            return False

meCar= Car()#to instantiate a class or create an object just use this type of code nameObject=nameClass()


print(meCar.startCar(True))#by using a dot after the object name you can access its attributes and methods
meCar.state()

print("---------------------")

meCar2=Car()
meCar2.state()




