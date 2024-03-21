''''
1. Funcție care să calculeze și să returneze suma a două numere
'''
from datetime import timedelta, datetime

def sum_2_numbers(a, b):
    return a + b

s = sum_2_numbers(15, 5)
print(s)


'''
2. Funcție care să returneze TRUE 
dacă un număr este par, FALSE pentru impar
'''
def is_even(nr):
    return nr % 2 == 0

nr = is_even(1235)
print(nr)


'''
3. Funcție care returnează numărul total de caractere 
din numele tău complet.
(nume, prenume, nume_mijlociu) 
'''

def full_name_len(first_name, last_name, middle_name):
    return len(first_name + last_name + middle_name)

full_name = full_name_len('Argeanu', 'Georgiana', 'Geo')
print(full_name)


'''
4. Funcție care returnează aria dreptunghiului
aria drept = l * L
'''

def rectangle_area(l, L):
    return l * L

print(rectangle_area(4, 6))


''''
5. Funcție care returnează aria cercului
aria cercului = pi * r^2
'''
import math


def circle_area(radius):
    return math.pi * radius ** 2


print(circle_area(5))


'''
6. Funcție care returnează True dacă un caracter 
x se găsește într-un string dat și False dacă nu găsește.
'''

def is_char_in_str(x, text):
    return x in text

print(is_char_in_str('a', 'banana'))
print(is_char_in_str('a', 'bete'))


'''
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y 
'''

def number_of_lower_and_upper_case(text):
    count_lower = 0
    count_upper = 0
    for char in text:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
    print(f'Numarul de caractere lower case este {count_lower} ')
    print(f'Numarul de caractereupper case este {count_upper} ')


number_of_lower_and_upper_case('Ana are mere fgghSDFGG')


'''
8. Funcție care primește o LISTĂ de numere și returnează 
o LISTĂ doar cu numerele pozitive.
'''

def get_all_positives(numbers):
    pozitives_numbers = []
    for elem in numbers:
        if elem > 0:
            pozitives_numbers.append(elem)
    return pozitives_numbers

print(get_all_positives([1, 2, 5, 9, 8, 10, -9, -6, -7]))


''''
9. Funcție care nu returneaza nimic. Primește două numere și 
PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. 
'''

def compare_numbers(x, y):
    if x > y:
      print(f'Primul nr {x} este mai mare decat al doilea nr {y}')
    elif x < y:
      print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
      print('Nr sunt egale')

compare_numbers(12, 11)
compare_numbers(10, 14)
compare_numbers(31, 31)


'''
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ 
+ returnează False
'''

def is_number_added_in_set(nr, numbers):
    if nr in numbers:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        numbers.add(nr)
        print('am adaugat numărul nou în set')
        return True

print(is_number_added_in_set(5,{1, 2, 3, 4}))
print(is_number_added_in_set(5,{1, 2, 3, 4, 5}))


'''
11. Funcție care primește o lună din an și returnează câte 
zile are acea lună.
'''

from calendar import monthrange
from datetime import datetime


def days_in_month(month):
    year = datetime.today().year  # anul si ziua de astazi
    # return monthrange(year, month)[1]
    weekday, month_days = monthrange(year, month)
    return month_days


print(days_in_month(9))
print(days_in_month(2))


'''
# 12. Funcție calculator care să returneze 4 valori.
# Suma, diferența, înmulțirea, împărțirea a două numere.
#
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
'''

def calculator(a, b):
    return a + b, a - b, a * b, a / b


a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


'''
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''


def count_digits(digits):
    dct = {}
    for i in range(10):
        dct[i] = 0 # setam nr de aparitii a fiecarei cifre la 0
    for elem in digits:
        #if elem in dct:
             dct[elem] += 1
        #else:
             dct[elem] = 1
    return dct


print(count_digits([1, 3, 1, 5, 9, 7, 7, 5, 5]))



'''
14. Funcție care primește 3 numere. 
Returnează valoarea maximă dintre ele.
'''
def maximum(x, y, z):
    return max(x, y, z)
print(maximum(5, 6, 8))



'''
15. Funcție care să primească un număr și să returneze suma 
tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
'''
def sum_until_nr(nr):
    s = 0
    for x in range(nr + 1):
        s += x
    return s
print(sum_until_nr(3))



'''
16.Funcție care primește 2 liste de numere 
(numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''

def common_numbers(lst1, lst2):
    return set(lst1) & set(lst2)   # intersectie &
print(common_numbers(lst1 = [1, 1, 2, 3], lst2 = [2, 2, 3, 4]))

# def common_numbers(lst1,lst2):
#     return set(lst1) & set(lst2) #intersectie
# print(common_numbers(lst1 = [1, 1, 2, 3],lst2 = [2, 2, 3, 4]))


'''
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. 
Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. 
De exemplu o reducere de 110% e invalidă.
'''

def apply_discount(price, discount):
    if 0 <= discount <= 100:
        return price - price * discount / 100
    print('Reducerea aplicata nu este valida')
print(apply_discount(100, 110))



'''
18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)
'''
def current_date_time():
    now = datetime.now()
    print(f'Romania: {now}')
    print(f'China: {now + + timedelta(hours = 6)} ')
print(current_date_time())




'''
19. Funcție care să afișeze câte zile mai sunt până la 
ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e 
ziua ta :)
'''

# def days_until_Christmas():
#     christmas_date_string = '25.12.1023'
#     christmas_date = datetime.strptime(christmas_date_string, '%d.%m.%Y')
#     today = datetime.today()
#     return (christmas_date - today).days
# print(days_until_Christmas())

def days_until_Christmas():
    christmas_date_string = '25.12.2023'
    christmas_date = datetime.strptime(christmas_date_string, '%d.%m.%Y')
    today = datetime.today()
    return (christmas_date - today).days
print(days_until_Christmas())
