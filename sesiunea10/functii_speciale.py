class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):  # le transf in string
        return f'Varsta: {self.age}, Nume: {self.name}'

    def __repr__(self):  # le transforma intrun string mai multe elem [a, b]
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False
        return self.name == other.name


d = Dog(1, 'Bolt')
print(d)
d2 = Dog(3, 'Spark')
l = [d, d2]
print(l)
d3 = Dog(2, 'Spark')
print(d2 == 7)
