class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height

    def __lt__(self, other):
        return self.volume() < other.volume()


c1 = Cuboid(2, 3, 4)
c2 = Cuboid(3, 3, 3)

print("Volume of Cuboid 1 =", c1.volume())
print("Volume of Cuboid 2 =", c2.volume())

if c1 < c2:
    print("Cuboid 1 is smaller than Cuboid 2")
else:
    print("Cuboid 2 is smaller than Cuboid 1")
