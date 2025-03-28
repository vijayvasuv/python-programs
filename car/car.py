#Declare a class
class Car:
    #Method to initiatilze attributes of car
    def __init__(self, color, make, model, type):
        self.color = color
        self.make = make
        self.model = model
        self.type = type
        self.mileage = 0

    #Method to change car color
    def change_color(self, value):
        self.color = value
        return self.color

    #Method to find miles driven
    def drive_car(self, miles):
        self.mileage+= miles
        return self.mileage

    #Method to print car details
    def describe_car(self):
        print(f"The car is a {self.color} {self.make} {self.model} {self.type}")

    #Method to print car mileage
    def read_mileage(self):
        print(f"The car has {self.mileage} on it.")

def main():
    #create instance for car class
    mycar = Car("Black", "Mercedes", "GLE450", "SUV")

    #access instance methods and print attributes
    mycar.describe_car()
    mycar.read_mileage()

    #access instance methods
    mycar.change_color("White")
    #add miles
    mycar.drive_car(50)

    #access instance methods and print attributes
    mycar.describe_car()
    mycar.read_mileage()

if __name__ == "__main__":
    main()
