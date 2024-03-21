class CustomException(Exception):
    pass


'''
Sa se scie o fct care verifica daca o lista de nr intregi
contine nr negative. Daca da sa se arunce o exceptie specifica
'''

class ContainsNegativeNumbersException(Exception):
    pass


def check_negative_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ContainsNegativeNumbersException(f'contine {number}')

check_negative_numbers([13, 2, 4, 8, -12])