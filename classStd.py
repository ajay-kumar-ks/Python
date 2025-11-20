class Person :
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        
class Marks:
    def __init__(self, Maths,Computer):
        self.Maths = Maths
        self.Computer = Computer
    def display(self):
        super().display()
        print('title => ',self.title)
        print('author => ',self.author)
        
class Student(Person,Marks) :
    def __init__(self, name, roll, Maths, Computer):
        Person.__init__(self, name, roll)
        Marks.__init__(self, Maths, Computer)
        
    def display(self):
        print("Name :", self.name)
        print("Roll :", self.roll)
        print("Maths Marks :", self.Maths)
        print("Computer Marks :", self.Computer)

        total = self.Maths + self.Computer
        percentage = total / 2

        print("Percentage :", percentage)

        if percentage >= 50:
            print("Result : PASS")
        else:
            print("Result : FAIL")
            
s1 = Student("ajay", 7, 10, 10)
s1.display()