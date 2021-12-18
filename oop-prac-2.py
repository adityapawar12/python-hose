# INHERITANCE
class Animal():

    def __init__(self):

        print("ANIMAL CREATED")

    def whoami(self):
        print("I am an animal.")

    def eat(self):
        print("I am eating.")
        
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED.")

    def whoami(self):
        print("I am a dog.")

    def bark(self):
        print("WOOF !")


myanimal = Animal()

myanimal.whoami()
myanimal.eat()

mydog = Dog()

mydog.whoami()
mydog.eat()
mydog.bark()

# POLYMORPHISM
class Animals():

    def __init__(self, name):

        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method.")


class Cat(Animals):

    def speak(self):
        return self.name + " says meow."


class Cow(Animals):

    def speak(self):
        return self.name + " says moo."

fido = Cat("fido")
cow = Cow("cow")

print(fido.speak())
print(cow.speak())
