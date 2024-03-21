'''
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
# x, y, z = 6, 8, 5
# if x == y != z or x == z != y or y == z != x:
#     print('Triunghiul este isoscel')
# elif x == y == z:
#     print('Triunghiul este echilateral')
# elif x != y != z:
#     print('Triunghiul este oarecare')
# else:
#     print('Invalid')


# 9. Citește o literă de la tastatură.
#     Verifică și afișează dacă este vocală sau nu.


'''
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
# note = int(input('Introdu nota'))
# if 10 <= note >= 9:
#     print('Nota A')
# elif 9 <= note >= 8:
#     print('Nota B')
# elif 8 <= note >= 7:
#     print('Nota C')
# elif 7 <= note >= 6:
#     print('Nota D')
# elif 6 <= note >= 4:
#     print('Nota E')
# elif note <= 4:
#     print('Nota F')


''''
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''


'''
12.Verifică dacă x are exact 6 cifre.
'''



''''
13.Verifică dacă x este număr par sau impar (x e int).
'''
# numar = 9
# if numar %2 == 0:
#     print('Numar este par ')
# else:
#     print('Numarul este impar ')


'''
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''
# x = 12345
# y = 6789
# z = 345
# if x > y and x > z:
#     print(f'Numarul cel mai mare este {x}')
# elif y > x and y > z:
#     print(f'Numarul cel mai mare este {y}')
# elif z > x and z > y:
#     print(f'Numarul cel mai mare este {z}')


'''
15. 
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
'''
# x, y, z = 90, 50, 60
# if x + y + z <= 180:
#     print('Triunghi valid')
# else:
#     print('Trunghi invalid')


'''
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
●	Citește de la tastatură un int x
●	Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
# string = 'Coral is either the stupidest animal or the smartest rock'
# x = 17
# print(string[:-x])

'''
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
'''
string = 'Coral is either the stupidest animal or the smartest rock'
print(string[:5] + string[-5:]) # primele 5 carac + ultimele carac


'''
18. Același string. 
●	Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
●	Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
●	output: 'Coral is either the stupidest animal or the smartest' 
'''
print(string.index('rock'))
i = string.index('rock')
print(string[:i])





