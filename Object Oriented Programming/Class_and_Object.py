class Car:
    total_car = 0
    def __init__(self, Brand, Model):
        self.__brand = Brand # to make a class variable private add __ before the name it will be accessible within the class only
        self.__model = Model
        Car.total_car += 1 # to keep track of number of objects created
        # self.total_car += 1 this will also work

# self is a telephone line that is used to establish connection in the class functions to access the variables

    def get_brand(self):
        return self.__brand + "!"
    
    def set_brand(self, brandName):
         self.__brand = brandName
         return self.__brand

#class method and self
    def carname(self):
        return f"Your car is {self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are a means of transport"
    
    @property
    def model(self):
        return self.__model

# my_car = Car()
# print(my_car.brand) # <__main__.Car object at 0x00000174310E6150> prints the car object's memory location

# instance of class Car
# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand, my_car.model) 

# print(my_car.carname())

# inheritance
class ElectricCar (Car):
    def __init__(self, Brand, Model, BatterySize):
        super().__init__(Brand, Model)
        self.BatterySize = BatterySize

    def fuel_type(self):
        return "electric charge"

myElectricCar = ElectricCar("Tesla", "Model S", "85kW")
# print(myElectricCar.brand, myElectricCar.model, myElectricCar.BatterySize) #Tesla Model S 85kW
print(myElectricCar.carname()) # Your car is Tesla Model S
# print(myElectricCar.brand) # Tesla 
print(myElectricCar.get_brand()) # Tesla!

# setter function
my_car = Car("Toyota", "Baleno")
print(my_car.carname()) # Your car is Toyota Baleno
print(my_car.set_brand("Maruti Suzuki")) # Maruti Suzuki
print(my_car.carname()) # Your car is Maruti Suzuki Baleno

# polymorphism
print(my_car.fuel_type()) # petrol or diesel
print(myElectricCar.fuel_type()) # electric charge

# my_car2 = Car("","")
print(Car.total_car) # outputs the total no of objects created

# print(my_car.general_desc()) # Cars are a means of transport
print(Car.general_desc()) # Cars are a means of transport
# my_car.model = "Alto"
print(my_car.model) # Baleno


print(isinstance(myElectricCar, Car)) # True
print(isinstance(myElectricCar, ElectricCar)) # True


class Battery:
    def battery_info(self):
        return "This is Battery class"

class Engine:
    def engine_info(self):
        return "This is Engine class"

class ElectricCar2(Battery, Engine, Car):
    pass

myNewElectricCar = ElectricCar2("Tesla", "Model X")
print(myNewElectricCar.battery_info()) # This is Battery class
print(myNewElectricCar.engine_info()) # This is Engine class