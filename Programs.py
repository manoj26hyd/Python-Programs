# Program to print average word length

class Student:

    def __init__(self):
        print("----------------------Welcome to the Student Portal---------------------")
        self.name = input("Enter Student Name : ")
        self.maths= input("Enter Student Maths Marks : ")
        self.physics = input("Enter Student Physics Marks : ")
        self.chemistry = input("Enter Student Chemistry Marks : ")
        self.display()

    def display(self):
        print("Your details are loading...............................")
        print("Student Name:", self.name)
        print("Maths:", self.maths)
        print("Physics:", self.physics)
        print("Chemistry:", self.chemistry)
        self.start_again()

    def start_again(self):
        response = input("Do you wish to continue[y/n]:")
        if response == "y":
            self.__init__()
        else:
            pass    

s1 = Student()
