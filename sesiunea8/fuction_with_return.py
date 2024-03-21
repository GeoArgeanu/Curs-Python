def say_hello():
    return 'Hello'  # fct se opreste din executie se va intarce in locul care a fost apelata dand inapoi val hellop

text = say_hello()
print(text)
print(say_hello())


def say_hi():
    print('Hi')
    return

text = say_hi()
print(text)