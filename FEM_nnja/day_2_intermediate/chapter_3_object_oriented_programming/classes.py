# ============================ self  ==========================
# Self is a reference to the new object that is being created, my_car or my_other_car


class Car():
    runs = False

    def start(self):
        if self.runs:
            print("The car is started. Vroom, vroom, let's go!")
        else:
            print("The car is broken.")


my_car = Car()
print(f"Runs is set to False: {my_car.runs}")
# Runs is set to False: False
my_car.start()
# The car is broken.

my_car.runs = True
print(f"Runs is later set to True: {my_car.runs}")
my_car.start()
# Runs is later set to True: True
# The car is started. Vroom, vroom, let's go!

my_other_car = Car()
my_other_car.start()
# The car is broken. --> Because this is another instance of Car() and refers to rhe original runs boolean False
