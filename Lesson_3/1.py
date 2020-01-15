""" 1.	В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

D = {}


def count_in_range(number, count=0, i=2,):
    """Функция считае количество появлений числа в диапазоне от 2 до 99"""
    while i in range(2, 100) != 100:
        if i % number == 0:
            count += 1
        else:
            pass
        i += 1
    return count


def range_number(number=2):
    """Функция перебирает числа в диапазоне и записывает в словарь"""
    while number in range(2, 10) != 10:
        D[number] = count_in_range(number)
        number += 1


range_number()
print(D)

# Вариант 2

DD = {}
N = 2
while N in range(2, 10):
    V = 0
    for f in range(2, 100):
        if f % N == 0:
            V += 1
    DD[N] = V
    N += 1

print(DD)
