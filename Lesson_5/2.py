"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
from functools import reduce


def summ(num_list):
    """Функция, переводит числа в десятичные,
    суммирует их и возвращает в виде шестнадцатиричного результата"""
    return hex(sum([int(''.join(i), 16) for i in num_list.values()]))[2:]


def multiply(num_list):
    """Функция, переводит числа в десятичные,
    перемножает их и возвращает в виде шестнадцатиричного результата"""
    return hex(reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in num_list.values()]))[2:]


if __name__ == '__main__':
    NUM_LIST = collections.defaultdict(list)

    for n in range(1, 3):
        d = input(f'Введите {n}-е шестнадцатеричное число: ')
        NUM_LIST[n] = list(d)
    # print(NUM_LIST)

    print(f'Сумма чисел = {summ(NUM_LIST)}\nПроизведение чисел = {multiply(NUM_LIST)}')
