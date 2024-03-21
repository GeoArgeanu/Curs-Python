'''
Decorators = fct in fct

Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții
logger – decorator care printeaza argumentele de intrare,
și rezultatul unei funcții
'''
import functools
from time import perf_counter, sleep


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'A durat {perf_counter() - start} secunde')
        return result
    return wrapper

@timeit
def say_hello():
    sleep(3)
    print('Functie executata')

say_hello()


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Rezultat: {result}')
        print(f'Argumente pozitionale: {args}')
        print(f'Argumente cu nume: {kwargs}')
    return wrapper

@logger
def name(first, last):
    return f'{first} - {last}'

name('Adrian', last = 'Andrei')


