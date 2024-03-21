class Dog:
    species = 'mamifer'  # acest tip de atribut este unul special ==> class, atribute
    age = 8
    name = 'Bruno'


d = Dog()  # instantierea unui obiect (d => obiect)

print(d.name)

d2 = Dog()
# d2.name = 'Puffy'  # name devine atribut de instanta pt ob d2
print(d.name, d2.name)

Dog.name = 'Rexy'
print(d.name, d2.name)


# atributele de clasa sunt in general folosite pt a defini
# constante intr-o clasa


class Cat:
    species = 'mamifer'

    def __init__(self, age, name):  # fct constructor
        # self este o referinta catre ob curent
        self.age = age
        self.name = name


c = Cat(1, 'Leo')
c2 = Cat(4, 'Mata')
print(c.age, c2.age)
# Cat.name  --> incorect deoarece atributul name
# este un atribut de instanta si poate fi accesat doar
# printrun ob din aceasta clasa
