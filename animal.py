class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, fname):
        self.name =  name
        self.fname = fname

    def replicate(self, name):
        pass

ani1 = Cat("Willy", "The Cat")
print(ani1.fname)