class Car:
    def __init__(self, wheels, model, brand):
        print("Create a new car!")
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.started = False
        
    def start(self):
        self.started = True

car = Car(4, "model", "brand")
print(car.model)
car.start()
print(car)
car2 = Car(4, "model2", "brand")
print(car2.model)
car3 = Car(4, "model3", "brand")
print(car3.model)
