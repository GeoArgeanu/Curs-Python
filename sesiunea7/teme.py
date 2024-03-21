'''
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
'''
numar_secret = input('Introdu un nr intre 1 si 30')
numar_ghicit = 0
while numar_ghicit > numar_secret:
    print(f'Nr secret e mai mic')
    if numar_ghicit < numar_secret:
        print('Nr secret e mai mare')
else:
    print('Felicitări! Ai ghicit!')



