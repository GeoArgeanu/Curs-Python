from contextlib import contextmanager


@contextmanager
def hello_context_manager():
    print('Intra in context')
    yield 'Hello World'
    print('Iesim din context')


with hello_context_manager() as h:
    print(h)
