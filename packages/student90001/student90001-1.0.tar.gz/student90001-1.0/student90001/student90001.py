class student:
    def __init__(self): #method
        self.name = input("Enter Your Name:") # attribute
        self.grade = input("Enter Your grades:") #attribute
        self.percentage = input("Enter Your percentages:")

    def student_details(self):
        print(f"{self.name} is in class {self.grade}")