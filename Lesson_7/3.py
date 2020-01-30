"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random
from statistics import median


def search_median(list):
    left = []
    right = []

    for i in range(len(list)):
        for k in range(len(list)):
            if list[i] > list[k]:
                left.append(list[k])
            if list[i] < list[k]:
                right.append(list[k])
            if list[i] == list[k] and i > k:
                left.append(list[k])
            if list[i] == list[k] and i < k:
                right.append(list[k])

        if len(left) == len(right):
            print(f'Медиана - {list[i]}')
            break
        left.clear()
        right.clear()


def main(m):
    list = [random.randint(0, 100) for i in range(2 * m + 1)]
    print(f"В массиве - {list}")
    search_median(list)
    print(f"Проверочное значение медианы: {median(list)}")


main(int(input("Введите число, которое сгенерирует массив: ")))
