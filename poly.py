class car:
    def sound(self):
        print("car sound...")
class truck:
    def sound(self):
        print("truuuuck sound...")

def makeSound(vechType):
    vechType.sound()

car1=car()
truck1=truck()


makeSound(car1)
makeSound(truck1) 
