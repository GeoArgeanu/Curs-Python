# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
#    Găsește 2 variante să le unești într-o singură listă.
numere1 = [3, 1, 0, 2]
numere2 = [6, 5, 4]
# 1
# numere.extend(numere1)
# print(numere)
# 2
print(numere1 + numere2)
numere = numere1 + numere2

# 4.
# ●	Sortează și afișează lista generată la exercițiul anterior.
# ●	Sortează numărul 0 folosind o funcție.
# ●	Afișaza iar lista.
numere.sort()
print(numere)
numere.sort(reverse=True)
print(numere)


# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ●	Lista este goală.
# ●	Lista nu este goală.
if numere == 0:
    print('Lista e goala')
else:
    print('Lists nu e goala')


# 6. Folosește o funcție care să șteargă lista de la exercițiul 3
numere.clear()
print(numere)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if list(numere) == 0:
    print('Lista e goala')
else:
    print('Lista nu e goala')


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print(list(dict1.keys()))


# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

print('Ana a luat nota de ', dict1.get('Ana'))
print('Gigel a luat nota de ', dict1.get('Gigel'))
print('Dorel a luat noata de ', dict1.get('Dorel'))


# 10. Dorel a făcut contestație și a primit 6
# ●	Modifică nota lui Dorel în 6
# ●	Printează nota după modificare

dict1['Dorel'] = 6
print(dict1)


# 11. Gigel se transferă din clasă
# ●	Căuta o funcție care să îl șteargă
# ●	Vine un coleg nou. Adaugă Ionică, cu nota 9
# ●	Printează noii elevi
dict1.pop('Gigel')
print(dict1)

dict1['Ionica'] = 9
print(dict1)

# 13.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ●	Adaugă în zilele_sapt ‘luni’
# ●	Afișează zile_sapt
zile_sapt = {'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)    # nu le afiseaza in ordine


# 14.Folosește un if și verifică dacă:
# ●	Weekend este un subset al zilelor din săptămânii.
# ●	Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print('Zile de weekend sunt incluse in zilele sapt')
elif weekend.issuperset(zile_sapt):
    print('Saptamana ccontine cele 7 zile')


# 15. Afișează diferențele dintre aceste 2 seturi.
diferenta = zile_sapt.difference(weekend)
print(diferenta)
diferenta1 = weekend.difference(zile_sapt)
print(diferenta1)


# 16. Afișează intersecția elementelor din aceste 2 seturi.
intersectia = zile_sapt.intersection(weekend)
print(intersectia)

