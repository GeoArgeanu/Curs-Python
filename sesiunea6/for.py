'''
O bucla for este folosita pentru a itera
peste o secventa (lista, tuplu, dictionar, set sau string)
'''
for i in range(10): # de la 0 la 9
    print(i)

print(20* '-')
for i in range(4, 10):  # de la 4 la 9
    print(i)

print(20* '-')
for i in range(4, 10, 2): # 4, 6, 8
    print(i)


print(20* '-')
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(l[i])


print(20* '-')
# for each
fructe = ['mere', 'pere', 'banane']
for x in fructe:
    print(x)

print(20* '-')
for x in 'Ana are mere':
    print(x)


print(20* '-')
# dictionary
# d = {
#     'a': 1,
#     'b': 2
# }
# for x in d:  # iteratia in dict se face inplicit prin chei
#     print(x)
# for x, value in d.items():
#     print(x, value)

# pentru dict
#  'a': 1,
#  'b': 2
# }
# d.keys()
# dict_keys(['a', 'b'])
# d.values()
# dict_values([1, 2])
# d.items()
# dict_items([('a', 1), ('b', 2)])

print(20* '-')
# break
for i in fructe:
    if x == 'pere':
        break
    print(x)

print(20* '-')
# continue
for x in fructe:
    if x == 'mere' or x == 'pere':
        continue
    print(x)


print(20* '-')
# for else
for x in fructe:
    print(x)
else:
    print('Sunt in else')


print(20* '-')
# else + break
for x in fructe:
    if x == 'pere':
        break
    print(x)
else:
    print('sunt in else')


print(20* '-')
# nested for
adj = ['rosii', 'mari', 'delicioase']
for x in fructe: # nu este folosit des e pacatos
    for y in adj:
        print(x, y)  # lung x * lung y dimensiunea listei 3*3


print(20* '-')
# pass
for x in [1, 2, 3]:
    pass  #  nu ruleaza nimic

for x in range(100_000_000):
    pass
print('gata')  # proceseaza 100000000 apoi arata gata