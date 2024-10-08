
class Animal:  # classe mere
    def __init__(self, name, color):
        self.name = name    # attr
        self.color = color

    def mange(self ,food):
        print("je mange du " ,food)


# **************************classe fille cat *********************
class Cat(Animal):
    def purr(self):
        print("Purr...")


# **************************classe fille dog *********
class Dog(Animal):
    def bark(self):
        print("Woof!")
    # **************************classe fille dog *********
class Mouse(Animal):
    def scream(self):
        print("mouse scream!")


# ***********************************************
fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
fido.mange("os")


f =  Cat("gros minet" ,'black and white')
print(f.color)
f.purr()
f.mange("fish")
