"""
Домашнее задание №1
Функции и структуры данных
"""



def power_numbers(*num):
    return [n ** 2 for n in num]


print(power_numbers(1, 3, 5, 6))

# filter types


def prime(i):
    if i == 1:
        return False
    test = True
    k = i - 1
    while k > 1:
        if not i % k:
            test = False
            break
        k -= 1
    return i if test else False


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


ODD = odd
EVEN = even
PRIME = prime


def filter_numbers(li, condition):
    return list(filter(condition, li))


print(filter_numbers([1, 2, 3], ODD))
print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([1, 2, 3, 4, 5, 7], PRIME))
