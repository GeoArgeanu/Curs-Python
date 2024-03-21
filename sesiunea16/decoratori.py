import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Inainte ca functia sa fie apelata')
        func()
        print('Dupa ce functia a fost apelata')

    return wrapper


def say_hi():
    print('Hi!')


say_hi = my_decorator(say_hi)
say_hi()
print(say_hi)


@my_decorator
def say_hello():
    print('Hello!')


say_hello()
print(say_hello)


# sa se scie un decorator care repeta executia unei fct de 2 ori

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@do_twice
def return_greeting(name):
    print('Create greeating')
    return f'Hi {name}'

r = return_greeting('Bob')
print(r)


'''
sa se scrie un decorator care executa o fct de n ori
n fiind un parametru al decoratorului
'''
def repeat(n):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(5)
def say_hello():
    print('Hello')

say_hello()
print(say_hello)

def say_hi():
    print('Hi')
d = repeat(5)
say_hi = d(say_hi)
say_hi()
print('-'*20)

repeat(5)(say_hi)()


'''
sa se scrie un decorator 
care intarzie apelalul unei fct cu o sec
'''
from time import sleep
def delay(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
         sleep(10)
         return func(*args, **kwargs)
    return wrapper
@delay
def string():
    print('Hello World')

string()
