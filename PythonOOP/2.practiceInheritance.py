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
    wheelie=""
    def makeWheelie(self):#you can add new attributes and methods to the new subclass
        self.wheelie="Doing a Wheelie"
    def state(self):# you can overwrite the methods to adjust them to your new class
        print("Mark: ",self.mark,"\nModel: ",self.model,"\nRunning: ",self.running,"\nAccelerate: ",self.accelerate,"\nBrake: ",self.brake,"\nWheelie: ",self.wheelie)

class Van(Vehicles):
    
    def load(self, load):
        self.loaded=load
        if(self.loaded):
            return "the van is loaded"
        else:
            return "the van is not loaded"

class ElectricVehicle(Vehicles):
    def __init__(self, mark, model):
        super().__init__(mark,model)
        self.autonomy=100
    def chargeEnergy(self):
        self.charging=True
    


meMotorcycle=Motorcycle("Honda","CBR")
meMotorcycle.makeWheelie()
meMotorcycle.state()

meVan=Van("ford","ab28")

meVan.starUp()
meVan.state()
print(meVan.load(True))

class ElectricBike(ElectricVehicle,Vehicles):#multiple inheritance , use the constructor of the first class introduced

    pass

meBike=ElectricBike("honda","cbr")

print("..............................")
meBike.state()


