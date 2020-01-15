"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random
N = 20
A = [0]*N
for i in range(N):
    A[i] = int(random() * 100)


def sort(number, array):
    """Функция сортирует массив от меньшего к большему"""
    number -= 1
    for idx in range(number):
        for j in range(number - idx):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(f"В массиве {sort(N, A)} \n два наименьших элемента {A[0], A[1]}")
