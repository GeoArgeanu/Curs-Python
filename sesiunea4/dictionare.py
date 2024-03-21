# creare
car = {
    'brand':'Ford',
    'model':'Mustang',
    'an': 1962
}

# accesarea elementelor
print(20* '-', 'accesarea elementelor', 20* '-')
print(car['brand'])
print(car.get('model'))
print(car.get('is_new'))
print(car.get('is_new', True))

# adaugare elemente
print(20* '-', 'adaugare elemente', 20* '-')
car['is_new'] = True
print(car)

car.setdefault('is_new', True)   # returneaza val de la cheia data daca aceasta nu esista va adauga val true (cea din paraneze)
car.setdefault('price', 7918)
print(car)


# stergere elem
print(20* '-', 'stergere elem', 20* '-')
car.pop('is_new')
print(car)

car.popitem()  # elimina ultima cheie inserata
print(car)

del car['an']
print(car)


# stergerea tuturor elem
print(20* '-', 'stergerea tuturor elem', 20* '-')
car.clear()
print(car)

# afisare toate chei
print(20* '-', 'afisare toate chei', 20* '-')
car = {
    'brand':'Ford',
    'model':'Mustang',
    'an':1962
}
print(list(car.keys()))
# toate valorile
print(list(car.values()))
# key - valoare
print(list(car.items()))
