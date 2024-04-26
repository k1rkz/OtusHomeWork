"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    print([n ** 2 for n in num])

power_numbers(1,3,5,6)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(i):
    if i % i == 0 and i != 0:
        return True
    else:
        return False
def filter_numbers(*list, condition):
    list.filter(condition == "odd" )

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
filter_numbers([1, 2, 3], ODD)