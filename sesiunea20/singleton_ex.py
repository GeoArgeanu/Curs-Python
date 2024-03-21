'''
singleton - sablon creational care se asigura ca o clasa are o singura
instanta si ofera acces universal catre aceasta instanta

AVANTAJE:
- POT SA FII SIGUR CA O CLASA ARE O SINGURA INSTANTA
- ACEEA INSTANTATA ESTE ACCESIBILA DIN COD
- ESTE INITIALIZATA DOAR CAND ESTE FOLOSITA PT PRIMA OARA

DEZAVANTAJE:
- POATE MASCA UN DESIGN SLAB EX ATUNCI CAND COMPONENTELE PROGRAMULUI SCRIU
PREA MULTE UNA DESPRE ALTA
'''


class SingletonLogger:
    _instance = None

    def __init__(self, filename):
        if hasattr(self._instance, 'filename'):
            return
        self.filename = filename

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating Object')
            cls._instance = super().__new__(cls)
        return cls._instance


logger = SingletonLogger('Hello.txt')
logger2 = SingletonLogger('Hello2.txt')
print(logger, logger2)

print(logger.filename, logger2.filename)
