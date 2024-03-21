'''
Listele sunt folosite pentru a stoca mai multe val intro singura variabila
Elem dintro lista sunt ordonate, modificabile si permit val duplicate
Listele sunt indexate si primul elem are index 0
Cand spunem ca o lista este ordonata : elem au o ordine predefinita si aceea ordine nu se va schimba
'''

# creare
fructe = ['mere', 'pere', 'banane']
numere = [1, 2, 3, 4, 5]
masini = list(('Audi', 'Tesla', 'Dacie'))

print(type(numere))
print(len(numere))

# indexare
# print(20* '-', 'indexare', 20* '-')
# print(numere[0])
# print(numere[-1])     #  primul de la capat
# print(numere[:2])     # de la inceput pana la index 1
# print(numere[::2])    # dn 2 in 2
# print(numere[:])    # dn 2 in 2
# print(numere[-1::-1])    # inversul listei

# adaugare element
print(20* '-', 'adaugare element', 20* '-')
numere.append(10)
print(numere)
numere.insert(2, 9)   # index, element
print(numere)

# stergere element
print(20* '-', 'stergere element', 20* '-')
elem = numere.pop()    # sterge de la final si il returneaza
print(elem)
print(numere)

numere.pop(0)  # elimina de la indexul specificat
numere.remove(3)  # elimina prima aparitie a volorii date

# stergere tuturor elementelor
print(20* '-', 'stergere toate element', 20* '-')
numere.clear()
print(numere)

# inlocuire element
print(20* '-', 'inlocuire element', 20* '-')
print(fructe)
fructe[1] = 'struguri'
print(fructe)


# numararea aparitilor
print(20* '-', 'numararea aparitilor', 20* '-')
numere = [1, 2, 3, 4, 5]
print(numere.count(2))

# adunarea a 2 liste
print(20* '-', 'adunarea a 2 liste', 20* '-')
numere2 = [20, 21, 22]
numere.extend(numere2)
print(numere)
numere3 = [1, 2, 3]
print(numere2 + numere3)  # nu se modifica nici una dintre liste

# inversare
print(20* '-', 'inversare', 20* '-')
# 1
print(fructe[::-1])  # nu modifica lista initiala
# 2
fructe.reverse()
print(fructe)  # modifica lista initiala (operatiune de in place)


# sortare
print(20* '-', 'sortare', 20* '-')
numere.sort()
print(numere)
numere.sort(reverse=True)
print(numere)