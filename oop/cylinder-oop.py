class Cylinder():

    def __init__(self, height = 1, radius = 1):

        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.height * (self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius*2)

        return (top * 2) + (2 * 3.14 * self.radius * self.height)


mycyl = Cylinder(2, 3)

print(mycyl.volume())
print(mycyl.surface_area())
