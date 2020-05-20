class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(self):
        return self.number_of_wheels

    def funcname(self):
        if self.runs:
            print("The car is started. Vroom, vroom, let's go!")
        else:
            print("The car is broken.")


my_car = Car()
print(f"Car --> number of wheels: {Car.get_number_of_wheels()}")
# Car --> number of wheels: 4

my_car.number_of_wheels = 6
print(f"my_car with more wheels --> {my_car.number_of_wheels}")
# my_car with more wheels --> 6

# Call classmethod on our instance my_car:
print(
    f"Classmethod called on instance my_class --> {my_car.get_number_of_wheels()}")
# Classmethod called on instance my_class --> 4

print(f"The type of my_car = {type(my_car)}")
# The type of my_car = <class '__main__.Car'>

# The isinstance() function takes an object and a class, and returns True if the object you pass it is an instance of the class:
print(isinstance(42, int))  # True
print(isinstance("Hello world!", str))  # True
print(isinstance(my_car, float))  # False
print(isinstance(my_car, Car))  # True
