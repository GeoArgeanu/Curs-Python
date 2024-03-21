def read(filename):
    with open(filename, 'r') as f:  # deschidere fisier in mod r (citire) si stocare ob in variabila f
        return f.readlines()

print(read('numere.txt'))


def write(filename, data):
    with open(filename, 'w') as f: # deschidere fisier din modul w ()
        f.writelines(data)

write('numere2.txt', ['1\n', '2\n', '3\n'])


def append(filename, data):
    with open(filename,'a') as f:
        f.writelines(data)


append('numere2.txt', ['1\n', '2\n', '3\n'])

