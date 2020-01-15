""" 4.	Определить, какое число в массиве встречается чаще всего."""

from random import random


def count_number(quantity, array):
    """Функция перебирает все элементы массива и выводит тот что встречается чаще"""
    number = array[0]
    max_count = 1
    for idx in range(quantity - 1):
        cur_count = 1
        for cnt in range(idx + 1, quantity):
            if array[idx] == array[cnt]:
                cur_count += 1
        if cur_count > max_count:
            max_count = cur_count
            number = array[idx]
    return max_count, number


def start():
    """функция создает массив, и выводит реультат проверки"""
    quantity = 20
    array = [0] * quantity
    for i in range(quantity):
        array[i] = int(random() * 100)

    max_count, number = count_number(quantity, array)
    if max_count > 1:
        print(f"В массиве {array} \nчисло {number} встречается {max_count} раз(а)")
    else:
        print(f"В массиве {array} все элементы уникальны")


start()
