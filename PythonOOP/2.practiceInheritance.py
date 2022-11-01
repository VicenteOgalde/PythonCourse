class Vehicles():
    def __init__(self, mark,model):
        self.mark=mark
        self.model=model
        self.running=False
        self.accelerate=False
        self.brake=False
    def starUp(self):
        self.running=True
    def speedUp(self):
        self.accelerate=True
    def braking(self):
        self.brake=True
    def state(self):
        print("Mark: ",self.mark,"\nModel: ",self.model,"\nRunning: ",self.running,"\nAccelerate: ",self.accelerate,"\nBrake: ",self.brake)
class Motorcycle(Vehicles):#by putting the name of the class in parentheses when creating a new class it inherits all the attributes and methods
    pass

meMotorcycle=Motorcycle("Honda","CBR")
meMotorcycle.state()

