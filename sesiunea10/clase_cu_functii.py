class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def bark(self):
        print('WOOF')

    def print_name(self):
        print(self.name)


d = Dog(4, 'Bruno')
d.bark()
d.print_name()
