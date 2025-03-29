#define a student class
class Student:
    #Initiatilize the attributes of Student class
    def __init__(self, name, age, city, school):
        self.name = name
        self.age = age
        self.city = city
        self.school = school

    #method to add attributes to a list
    def add_student(self, note):
        self.note = []
        self.note.append(self.name)
        self.note.append(self.age)
        self.note.append(self.city)
        self.note.append(self.school)

    #method to print the student list
    def show_student(self):
        #unpack the list and print with a , separator
        print(*self.note, sep = ",")

def main():
    #create an instance for the student class
    my_entry = Student("Saru", 33, "Dallas", "UT Arlington")
    #call instance method to add items to list
    my_entry.add_student(my_entry)
    #call instance method to print the student list
    my_entry.show_student()


if __name__ == "__main__":
    main()
