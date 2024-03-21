'''
Decorators extra
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii
– o metoda login, care va primi email și parola ca parametrii;
dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile
despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login`
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare,
dupa delogare, și după încă o logare.
'''
import functools


def require_logged_in(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_logged_in:
            return func(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.__logat = False

    def login(self, email, parola):
        if email == self.email and parola == self.parola:
            self.__logat = True

    @require_logged_in
    def get_info(self):
        return f' Nume: {self.nume},\n Email: {self.email},\n Data nasterii: {self.data_nasterii},\n Parola: { "*" * len(self.parola)}'

    def logout(self):
        self.__logat = False

    @property
    def is_logged_in(self):
        return self.__logat


u = User('Adrian Andrei', 'adrianandrei@gmail.com', 'parola123', '01.09.90')
print(u.get_info())
u.login('adrianandrei@gmail.com', 'parola123')
print(u.get_info())
u.logout()
print(u.get_info())
