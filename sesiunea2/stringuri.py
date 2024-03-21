# lunimea unui string
name = 'Dragos'
print(len(name))

# convertire la uppercas
print(name.upper())  # il transforma in litere mare

# convertire la lowercase
name = 'DrAgOS'
print(name.lower())  # litere mici

# numar de aparitii
nume = 'Ana Maria'
print(nume.count('a'))
print(nume.count('i'))
print(nume.count('t'))

# inlocuire de text
prop = ' - Oare vreau sa merg acolo! \n - Unde sa mergi !'
print(prop)  # \n - caracter pentu linia noua
print(prop.replace('!', '?'))
print(prop)  # fct replace nu modifica stringul intial

# index
name = 'John'
print(name.index('o'))  # gaseste indexul primei potriviri cu caracterul din paranteze
print(name[0])
print(name[-1])  # ultimul caracter

# slicing
b = 'Hello, world!'
print(b[2:5])  # de la 2 a 5 (fara 5)
print(b[:5])  # de la inceput pana la 5
print(b[2:])  # de la 2 pana la final
print(b[-5:-2])  # indecsare negativa
