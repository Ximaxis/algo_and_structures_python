"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint
import timeit

L = int(input("Введите длинну массива "))
LIST = [randint(-100, 100) for _ in range(L)]
print(f"Оригинальный список \n{LIST}")


def bubble_sort(list, lens):
    """
    Функция сортирует по убыванию методом "пузырька"
    """
    for i in range(lens):
        for j in range(lens - i):
            if list[j] < list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]

    return list


def bubble_sort_2(list, lens):
    """
    Доработаная функция сортировки пузырька,
    в ситуации когда нечего изменять в массиве функция завершается досрочно
    """
    for i in range(lens):
        mod = False
        for j in range(lens - i):
            if list[j] < list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]
                mod = True
        if not mod:
            return list
    return list


print("Время выполнения обычного `пузырька`")
print(timeit.timeit("bubble_sort(LIST, L-1)",
      setup="from __main__ import bubble_sort, LIST, L", number=1000))
print("Время выполнения модифицированого `пузырька`")
print(timeit.timeit("bubble_sort_2(LIST, L-1)",
      setup="from __main__ import bubble_sort_2, LIST, L", number=1000))

print(f"Отсортированый список \n{LIST}")

"""
Доработаная функция работает быстрее оригинальной в разы
при массиве в 100 чисел на 1000 запусков разница во времени в 50 раз
при массиве в 1000 чисел на 1000 запусков разница во времени более 300 раз
"""
