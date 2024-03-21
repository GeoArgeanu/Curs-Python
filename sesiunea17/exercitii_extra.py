'''
1. Sa se scrie un decorator care primeste ca parametru doua ore,
reprezentand datele limita intre care sa se execute functiile decorate.
'''
import functools
from contextlib import contextmanager
from datetime import datetime
from time import perf_counter, sleep


def only_execute_between(start, end):
    def decorator_execute_between(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if start <= datetime.now().hour <= end:
                return func(*args, **kwargs)

        return wrapper

    return decorator_execute_between


@only_execute_between(19, 23)
def hello():
    print('Hello World!')


hello()



'''
2. Sa se scrie un context manager care masoara durata de 
executie a codului din interiorul sau
'''


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'A durat {perf_counter()} - {self.start} secunde ')


with Timer():
    sleep(3)
    print('M-am trezit')


@contextmanager
def timer():
    start = perf_counter()
    yield
    print(f'A durat {perf_counter() - start}')


with timer():
    sleep(3)
    print('M-am trezit!')

'''
3. Sa se scrie un generator care primeste ca parametru un string si 
genereaza cate un caracter in ordine inversa a aparitiei in string
'''


def rev_str_gen(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]


for elem in rev_str_gen('abcd'):
    print(elem)
