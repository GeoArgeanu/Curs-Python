'''
O clasa abstracta este o clasa care are cel piutin o met abstracta
o metoda abstracta este o metoda fara implementate (fara corp)
'''

from abc import ABC, abstractmethod  # abc = abstract class


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):

    def sound(self):
        print('Woof')

    def sleep(self):
        print('Zzzz')