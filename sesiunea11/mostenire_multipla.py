class Car:
    def go(self):
        print('Vrum, Vrum')

    def start(self):
        print('Starling car')

class Flyable:
    def fly(self):
        print('Fly, Fly')
    def start(self):
        print('Starling Flyble')

class Flying(Car, Flyable):
    pass
c = Flying()
c.go()
c.fly()
c.start()

# MRO -> method resolution order: se decide care fct din clasa Car sau
# Flyable se va apela (de la stanga la dreapta)