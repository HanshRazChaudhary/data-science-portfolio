# Creating Class:
class Car:
    # Creating Variable To Keep Count:
    totalCar = 0
    # Creating A Constructor:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand            # Making Brand Private Using Encapsulation
        self.__model = usermodel            # Making Brand Private Using Encapsulation
        Car.totalCar += 1

    #Creating Another Method For Polymorphism:
    def fuel_type(self):
        return "Petrol or Disel"

    # Creating Getter Method:
    def get_userbrand(self):
        return self.__brand + " !"
   
    # Creating Function Inside The Class:
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    # Creating Static Method:
    @staticmethod
    def general_description():
        return "Car Is Means Of Transportation"
    
    # Creating Method For Setter and Using Property Decorators:
    @property           # Propert Decorators Does Not Let Us Change Nay Value
    def model(self):
        return self.__model
    
# Inheritance:
class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, userBatteySize):
        # Inherting Value From Car Class:
        super().__init__(userbrand, usermodel)
        self.battery = userBatteySize

    #Creating Method For Polymorphism:
    def fuel_type(self):
        return "Electricity"

# Creating Object From ElectricCar Class:
my_tesla = ElectricCar("Tesla", "Model S", "85KMWH")

# Checking Instance Of my_tesla:
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(my_tesla.full_name())
# print(my_tesla.model)     ---> Cannot Be Accesed Not We Have To Use get_brand Method 
print(my_tesla.battery)

# Getting Value Using Polymorphism:
print(my_tesla.fuel_type())

# Accessing Get Brand Method:
print(my_tesla.get_userbrand())

# Creating Object With Help Of Class
myCar = Car("BMW", "S-Class")

# Accessing Value Of Object From Class
# print(myCar.brand)        ---> Cannot Be Accesed Not We Have To Use get_brand Method 
print(myCar.model)              
print(myCar.full_name())

# Getting Value Using Polymorphism:
print(myCar.fuel_type())

# Print Total Car Count:
print(Car.totalCar)

# Accessing Value From Object From Static Method:
# print(myCar.general_description())        ---> Can Not Access Static Method From Object
print(Car.general_description())            # Only Accessed By Class 

# Changing Value Of Objects: 
# myCar.model = "Lambo"         ---> Cannot Change The Value Cause We Set Setters
print(myCar.model)


# MULTIPLE INHERITENCE
class Battery:
    def battery_info(self):
        return "This Is A Batery!"
    
class Engine:
    def engine_info(self):
        return "This Is A Elctric Engine!"
    
class ElectricCarTwo(Car, Battery, Engine):
    pass

# Creating Object:
myNewTesla = ElectricCarTwo("Tesla", "Model S")

# Accessin Multiple Class Value At Once:
print(myNewTesla.battery_info())
print(myNewTesla.engine_info())