# 1. variabila => o zona din memoria calculatorului care tine date


nume = 'Alexandru'  # string
note_elev = 10  # int = nr intreg
medie_note = 9.50  # float = nr zecimal
admis = True  # True False

medie_note = 9.89 # suprascriere
print(round(medie_note))

print(type(nume), type(note_elev), type(medie_note), type(admis) )
print(f'Numele elevului este  {nume}  nota de la teza e  {note_elev}  cu media finala de {medie_note} si este {admis}')

firs_name = 'Argeanu'
last_name = 'Georgiana'

print(firs_name, last_name)
x = len(firs_name) + len(last_name)
print(f'Numele complet are {x} caractere')
