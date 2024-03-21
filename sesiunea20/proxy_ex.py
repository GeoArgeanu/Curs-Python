'''
PROXY este un sablon structural care te lasa sa oferi un substitut
pt alt obiect
O clasa proxy controleaza accesul la obiectul original permitand
niste actiuni inainte sau dupa ce se realizeaza actiunea obiectului original

AVANTAJE:
- poti controla ob original ara ca cel care ilolosesc sa stie detalii despre acesta
- poti gestiona ciclul de viata al ob original fara a afecta clasele care il utilizeaza
- clasa proxy functioneaza si dac ob original nu este pregatit sau nu este disponibil

DEZAVANTAJE:
- codul poate devini mai complicat dearece este nevoie de a introduve mai multe clase
- raspunsul de la ob original poate fi intarziat din cauza clase proxy
'''

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print('Real subject: ma ocup de request.')

class Proxy(Subject):
    def __init__(self, rs):
        self.real_subject = rs
    def check_acces(self):
        print('proxy: Verificam acces pt request')
        return True
    def log_request(self):
        print('Proxy: se afiseaza timpul requestului')

    def request(self):
        if self.check_acces():
            self.real_subject.reqest()
            self.log_request()

rs = RealSubject()
rs.request()
print(50 * '*')