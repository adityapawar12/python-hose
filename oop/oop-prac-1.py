class Dog():

    # CLASS OBJECT ATTRIBUTE.
    # Same for any instance of class
    species = 'mamal'

    def __init__(self, name, breed, spots):

        # Attributes
        # we take in arguments of the init function/method.
        # and then assign them as class attributes using the self.attribute_name syntax.
        self.name = name
        self.breed = breed
        self.spots = spots

    # Method > action/operation
    def bark(self, number):
        print(f'WOOF! My name is {self.name} and the number is {number}.')

    
my_dog = Dog(name = 'zippy', breed = 'lab', spots = True)

print(type(my_dog))
print(my_dog.species)
print(my_dog.name)
print(my_dog.breed)
print(my_dog.spots)
my_dog.bark(109)

class Circle():

    # CLASS OBJECT ATTRIBUTE.
    pi = 3.14

    def __init__(self, radius = 1):

        self.radius = radius
        self.diameter = radius * 2
        self.area = Circle.pi * radius * radius

    def get_circumference(self):
        print(f"circumference of the circle is {self.radius * self.pi * 2}")


my_circle = Circle(12)

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.diameter)
print(my_circle.area)
print(my_circle.get_circumference())
