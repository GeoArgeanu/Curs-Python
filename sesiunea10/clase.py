'''
O clasa este o schita sau un prototip definit de programatpor din care sunt create ob.
Clasele ofera un mijl de a grupa datele si functionalitatile.
Crearea unei clase noi creaza un nou tip de obiect, permitand instatierea unor obiecte din acest tip.
Fiecare instanta de clasa poate avea atribuite atasate pt mentinerea starii sale.
Instantele de clasa pot avea si metode pt modificarea starii lor.
Un obiect este instanta unei clase.
Diferenta dintre obiect si clasa: o clasa este ca o schita in timp ce un ob este o copie a clasei cu val reale.
'''

class Dog:
    species = 'mamifer'
    age = 8
    name = 'Bruno'

d = Dog() # instantierea unui obiect (d => obiect)
print(type(d))
print(d.species)
print(d.age)
print(d.name)
