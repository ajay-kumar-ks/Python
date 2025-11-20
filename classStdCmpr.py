class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class Marks:
    def __init__(self, Maths, Computer):
        self.Maths = Maths
        self.Computer = Computer


class Student(Person, Marks):
    def __init__(self, name, roll, Maths, Computer):
        Person.__init__(self, name, roll)
        Marks.__init__(self, Maths, Computer)

    def percentage(self):
        return (self.Maths + self.Computer) / 2

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Maths:", self.Maths)
        print("Computer:", self.Computer)
        print("Percentage:", self.percentage())

        if self.percentage() >= 50:
            print("Result: PASS")
        else:
            print("Result: FAIL")
        print("-" * 30)


s1 = Student("Ajay", 6, 60, 40)
s2 = Student("Adon", 7, 80, 90)

s1.display()
s2.display()

if s1.percentage() > s2.percentage():
    print(f"{s1.name} has a higher percentage than {s2.name}.")
elif s2.percentage() > s1.percentage():
    print(f"{s2.name} has a higher percentage than {s1.name}.")
else:
    print("Both students have equal percentage.")
