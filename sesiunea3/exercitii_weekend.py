lungimea = 15
latimea = 10
x = lungimea * latimea
print(f'Aria dreptunghiului este de {x}')

articol = 'Coral is either the stupidest animal or the smartest rock'
print(articol.count('the'))

nume = 'Argeanu'
print(len(nume))
print(nume[3])

print('alabala portocala')
x, y = 'aLaBAla', 'pORtOcaLA'
print(x)
print(y)
print(x.upper())
print(y.upper())

user = 'argeanu'
parola = 'edfhgtyfsasf'
x = len(parola)
print(f'Parola pentru userul {user} are {x} caractere')


# x, y, z = 6, 8, 5
# if x == y != z:
#     print('Triunghiul este isoscel')
# elif x == z != y:
#     print('Triunghiul este isoscel')
# elif y == z != x:
#     print('Triunghiul este isoscel')
# elif x == y == z:
#     print('Triunghiul este echilateral')
# elif x != y != z:
#     print('Triunghiul este oarecare')
# else:
#     print('Invalid')


note = int(input('Introdu nota'))
if 10 <= note >= 9:
    print('Nota A')
elif 9 <= note >= 8:
    print('Nota B')
elif 8 <= note >= 7:
    print('Nota C')
elif 7 <= note >= 6:
    print('Nota D')
elif 6 <= note >= 4:
    print('Nota E')
elif 4 <= note >= 0:
    print('Nota F')
else:
    print('Nota invalida')


nr = 1135
if nr % 2 == 0:
    print('numar par')
else:
    print('numarul este impar')



