# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def ujj(Coding):
    print(f'Hobbies,{Coding}')


ujj("Hack")

class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def drive(self):
         print(f"{self.model} {self.year} driving since")

    def gasoline(self):
        print(f"{self.model} is in petrol station and petrol in being put")

    def stop_drive(self):
        print(f"{self.model} {self.year} now stopped driving")


# inheritance
class ElectricCar(Car):
    def __init__(self, model, year):
        super().__init__(model,year)

    def electricCharge(self):
        print(f"{self.model} is in Charging station and is being charged up 90% charge complete")



my_mercedes = Car('GLS','2023')

print(f"My car model is {my_mercedes.model}")
print(f"My car DOB is {my_mercedes.year}")
my_mercedes.drive()
my_mercedes.stop_drive()



# inheritance
my_tesla = ElectricCar("Cybertruck","2024");
my_tesla.drive()
my_tesla.electricCharge();
