"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    print([n ** 2 for n in num])


print("Квадраты чисел")
power_numbers(1, 3, 5, 6)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def prime(i):
    for el in i:
        if el % el == 0 and el != 0:
            return True
        else:
            return False


def even(i):
    if i % 2 == 0:
        return True
    else:
        return False


def odd(i):
    if i % 2 != 0:
        return True
    else:
        return False


def filter_numbers(num, condition):
    print(condition)
    return print(list(filter(condition, num)))

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """


# filter_numbers([1, 2, 3], ODD)
# filter_numbers([2, 3, 4, 5], EVEN)
filter_numbers([1, 2, 3, 4, 5, 7], PRIME)
