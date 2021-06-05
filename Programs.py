# Program to print average word length

class Student:

    def __init__(self):
        print("----------------------Welcome to the Student Portal---------------------")
        self.name = input("Enter Student Name : ")
        self.maths= int(input("Enter Student Maths Marks : "))
        self.physics = int(input("Enter Student Physics Marks : "))
        self.chemistry = int(input("Enter Student Chemistry Marks : "))
        self.calc()

    def display(self):
        print("Your details are loading...............................")
        print("Student Name:", self.name)
        print("Maths:", self.maths)
        print("Physics:", self.physics)
        print("Chemistry:", self.chemistry)
        print("Average Marks:", self.average)
        self.start_again()

    def calc(self):
        self.average = (self.maths + self.physics + self.chemistry)/3
        self.display()

    def start_again(self):
        response = input("Do you wish to continue[y/n]:")
        if response == "y":
            self.__init__()
        else:
            pass    

s1 = Student()