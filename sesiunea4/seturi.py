# seturile sunt colectii de elemente unice si neordonabile

# creare
print(20* '-', 'creare', 20* '-')
fructe = {'mar', 'para', 'banana'}
masini = set() # asa se creaza un set fara nici un element


# adaugare elemente
print(20* '-', 'adaugare elemente', 20* '-')
fructe.add('struguri')
print(fructe)


# stergere elem
print(20* '-', 'adaugare elemente', 20* '-')
fructe.remove('banana')
print(fructe)
#fructe.remove('cirese') # nu exista in set arunca erori
#print(fructe)
fructe.discard('cirese') # nu arunca eroare
fructe.pop()
print(fructe)

fructe.clear()
print(fructe)


# Operatii speciale
# 1. Join
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print(set1 | set2)

# 2. Intersectia
x = {'apple', 'banana', 'cherry'}
y = {'goole','microsoft','apple'}
z = x.intersection(y)
print(z)
print(x & y)

# 3. Diferenta
x = {'apple', 'banana', 'cherry'}
y = {'goole','microsoft','apple'}
z = x.difference(y)
print(z)
print(x - y)
print(y - x)


# 4. Diferenta simetrica
x = {'apple', 'banana', 'cherry'}
y = {'goole','microsoft','apple'}
z = x.symmetric_difference(y)  # toate elem care nu sunt comune
print(z)
print(x ^ y)

# 5. subset si super set
a = {1, 2, 3}
b = {5, 4, 3, 2, 1}
print(a.issubset(b))   # toate elem lui a sunt in b
print(b.issuperset(a))  # b contine toate elem lui a
