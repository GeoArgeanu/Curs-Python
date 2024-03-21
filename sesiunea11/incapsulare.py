'''
3 tipuri de metode si atibute:
  - public  accesibile peste tot
  - private  accesibile doar in clase (__atribute)
  - protected  accesibil in ierarhia de mostenire (_atribute)
'''


class Car:
    __model = 'Dacia'

    def get_model(self):  # get pt a returna model
        return self.__model

    def set_model(self, value):  # set pt a schimba val curenta din model
        self.__model = value


c = Car()
print(c.get_model())
c.set_model('Bmw')
print(c.get_model())


class Plain:
    __color = 'Red'

    @property  # functioneaza ca si un getter
    def color(self):
        print('setting a property')
        return self.__color

    @color.getter
    def color(self):
        print('Getting value')
        return self.__color

    @color.setter
    def color(self, value):
        print('Setting value: ')
        self.__color = value

    @color.deleter
    def color(self, value):
        print('Deleting value: ')
        self.__color = None

    @property
    def is_painted(self):
        return self.__color is not None

p = Plain()
print(p.color)
p.color = 'Blue'
print(p.color)
#del p.color
print(p.color)
print(p.is_painted)
