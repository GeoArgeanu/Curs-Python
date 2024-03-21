class Animal:
    def __init__(self, age, specie):
        self.age = age
        self.specie = specie

    def eat(self):
        return f'Eu sunt {self.__class__.__name__} {self.specie} mancacios'


class DomesticalAnimal(Animal):
    def __init__(self, age, specie, owner):
        super().__init__(age, specie)
        self.owner = owner


class WildAnimal(Animal):
    def __init__(self, age, specie, location):
        super().__init__(age, specie)
        self.location = location


def animals_eat(animals):
    for a in animals:
        print(a.eat())


animals_eat([
    DomesticalAnimal(5, 'vaca', 'Ion'),
    DomesticalAnimal(3, 'caine', 'Ion'),
    WildAnimal(40, 'URS', 'Padure'),
    WildAnimal(25, 'Girafa', 'Padure')
])

'''
* Polimorfismul se refera la abilitatea unui ob de a se comporta 
in mai multe moduri in functie de context.
* In esenta polimorfismul permite obiectelor de acelasi tip sa aibe comportamente 
deferite fara a fi necesar sa se stie tipul lor inainte de executie.
'''
