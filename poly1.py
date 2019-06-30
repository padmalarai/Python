class car:
    def __init__(self,name):
        self.name=name
 
class sportsCar(car):
    def drive(self):
        return 'sports car driving'
    def speed(self):
        return 'sports car speeding'

class jeep(car):
    def drive(self):
        return 'jeep driving'
    def speed(self):
        return 'jeep speeding'

obj1=[sportsCar("sCar"),jeep("thar")]

for obj in obj1:
    print(obj.name+":"+obj.drive())
    print(obj.name+":"+obj.speed())
    print("*"*20)
