class Car():
    def run(self):
        print("run on 4 wheels")

class Bike():
    def run(self):
        print("run on 2 wheels")

class Truck():
    def run(self):
        print("run on 6 wheels")

def runVehicle(Vehicle):# here receives an object and uses the method according to the type of object entered, using polymorphism
    Vehicle.run()

meVehicle=Truck()

runVehicle(meVehicle)


