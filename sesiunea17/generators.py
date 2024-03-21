'''
Generators = sub forma de functie (yield)

Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
'''
from random import randint


def loterie_g():
    for i in range(6):
        yield randint(1, 49)
    yield randint(1_000_000, 9_999_999)


for i in loterie_g():
    print(i)



# pentru a ne asigura ca sunt 6 nr unice
def loterie_gen_unice():
    generate = set()
    for i in range(6):
        nr = randint(1, 49)
        while nr in generate:  # cat timp nr generat a mai fost generat inca o data pana acum
            nr = randint(1, 49)
        generate.add(nr)  # adauga nr nou in setul de nr generate pana acum
        yield nr
    yield randint(1_000_000, 9_999_999)


for i in loterie_g():
    print(i)
