def product(a, b):
    return a * b


p = product(2, 3)
print(p)


def is_even(number):
    # if number % 2 == 0:
    #     return True
    # return False
    return number % 2 == 0


def get_all_even_numbers(numbers):
    result = []
    for elem in numbers:
        # if elem % 2 == 0:
        if is_even(elem):
            result.append(elem)
    return result


nr = get_all_even_numbers([1, 2, 5, 6, 7, 10, 30])
print(nr)
