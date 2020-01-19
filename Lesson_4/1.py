"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile
import timeit
import random

# Первый алгоритм

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


def start1():
    """функция создает массив, и выводит реультат проверки"""
    quantity = 100
    array = [0] * quantity
    for i in range(quantity):
        array[i] = int(random.random() * 100)

    max_count, number = count_number(quantity, array)
    if max_count > 1:
        pass
    else:
        pass

# Второй алгоритм

def start2():
    """функция перебирает все элементы массива
    и записывает число с максимальным количеством повторений"""
    list = [random.randint(-100, 100) for i in range(100)]
    num = max(list, key=list.count)


# print(timeit.timeit(start1))
# print(timeit.timeit(start2))

print(timeit.timeit('start1()',
                    setup='from __main__ import start1',
                    number=10000))

print(timeit.timeit('start2()',
                    setup='from __main__ import start2',
                    number=10000))
"""
Взял алгоритм с 3 урока, считающий максимальное количество появление числа
Алгоритм start1 имеет сложность квадратичную O(n)^2 а start2 имеет линейную сложность О(n)
если их сравнить по получается следующая закономерность:
при числе элементов 5 start1 = 8.96 сек start2 = 16.5 сек
без ограничения запусков при большем числе элементов выходит очень долго,
потому введу ограничение на 10000 запусков
при числе элементов 5 start1 = 0.075 сек start2 = 0.139 сек
при числе элементов 20 start1 = 0.56 сек start2 = 0.73 сек
при числе элементов 50 start1 = 2.59 сек start2 = 1.92 сек
при числе элементов 100 start1 = 8.64 сек start2 = 4.61 сек
и для завершения
при числе элементов 1000 start1 = 768.47 сек start2 = 266.61 сек
"""
cProfile.run(f"start2()")
