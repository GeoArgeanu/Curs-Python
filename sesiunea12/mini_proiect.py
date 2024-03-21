'''
Creati o clasa abstracta numita Gradinita care sa mosteneasca clasa
ABC (abstract base class) si sa aiba urmatoarele metode:

activitate_practica()
ora_de_somn()

Corpul primei metode va fi “pass” iar corpul celei de-a doua
metode va contine un raise NotImplementedError
(estimeaza cineva ce inseamna acest raise NotImplementedError?).

Fiecare din cele doua metode vor avea decoratorul @abstractmethod
(ce este un decorator?)

'''
from abc import ABC, abstractmethod
from pprint import pprint


class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError


'''
Implementati doua clase: GradinitaPublica si GradinitaPrivata 
care sa implementeze (mosteneasca) clasa abstracta Gradinita. 
'''


class GradinitaPublica(Gradinita):
    def activitate_practica(self):
        print('Copii invata sa deseneze')

    def ora_de_somn(self):
        print('Copii trebuie sa doarma la ora 5')


class GradinitaPrivata(Gradinita, ABC):
    __elevi = {}

    def _adauga_elev(self, **kwargs):
        self.__elevi.update(kwargs)

    @property
    def elevi(self):
        return self.__elevi

    @elevi.setter
    def elevi(self, value):
        self._adauga_elev(**value)

    def activitate_practica(self):
        print('Copii invata sa modeleze cu plastilina')

class GradinitaPrivata11(GradinitaPrivata):
    def ora_de_somn(self):
        print('ghh')

class GradinitaPublica25(GradinitaPublica):
    numar_elevi = 600
    _adresa = 'Srt. Napoca nr. 12'
    __fonduri = 300_000

    @property
    def fonduri(self):
        return self.__fonduri

    @fonduri.setter
    def fonnduri(self, value):
        self.__fonduri = value

    @fonduri.deleter
    def fonduri(self):
        self.__fonduri = None

    def activitate_practica(self):
        print('Copii se joaca in curte pe balansoar')

    def calculeaza_medie_buline_rosii(self, buline):
        media = sum(buline) / len(buline)
        if media > 5:
            print('Elevii acestei gradinite sunt foarte neastamparati')

    def info_elevi(self):
        elevi = {}
        while True:
            nume_elev = input('Introdu numele elevului: ')
            nume_parinti = input('Introdu nue parinti: ')
            varsta = input('Introdu varsta: ')
            activitate = input('Introdu act preferata: ')
            elevi[nume_elev] = {
                'nume_parinti': nume_parinti,
                'varsta': varsta,
                'activitate': activitate
            }
            introduce = input('Doresti sa introduci date in continuare? (y/n)')
            if introduce.lower() != 'y':
                break
        pprint(elevi)


p = GradinitaPublica()
p.activitate_practica()

# pr = Gradinita_privata  --> da eroare pt ca nu se pot crea ob pt clase abstracte

p25 = GradinitaPublica25()
p25.activitate_practica()
p25.ora_de_somn()

p25.calculeaza_medie_buline_rosii([1, 2, 3, 4])
p25.calculeaza_medie_buline_rosii([8, 9, 10])

# p25.info_elevi()

# print(p25.numar_elevi)
# print(p25.fonduri)
# p25.fonduri = 120_000
# print(p25.fonduri)

# del p25.fonduri
# print(p25.fonduri)


pr11 = GradinitaPrivata11()
pr11.elevi = {'Andrei' : {'varsta' : 3, 'an inscriere' : 2022}}
pr11.elevi = {'Maria' : {'varsta' : 4, 'an inscriere' : 2021}}
pprint(pr11.elevi)