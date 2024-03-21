'''
21. Având stringul '0123456789'
●	Afișează doar numerele pare
●	Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
'''
# string = '0123456789'
# print(string[::2])  # de la 0 : pana la capat : apoi pasul 2 (par)
# print(string[1::2]) # de la 1 : pana la capat : apoi pasul 2 (impar)



'''
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''
# string = input('Introdu un string: ')
# assert string[0].lower() == string[-1].lower()


'''
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
●	19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
●	Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
●	Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
●	Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
●	Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
●	Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''
import random
zar = random.randint(1,6)
incercare = int(input('Introdu un nr intre 1 si 6 '))
if incercare < zar:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {incercare} dar a fost {zar}')
elif incercare > zar:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {incercare} dar a fost {zar}')
else:
   print('Ai ghicit. Felicitări!')





