"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit


def simple_number_list(desired):
    n = desired * 8
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                if len(lst) == desired:
                    return lst[desired - 1]
                else:
                    lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)


def sieve_eratosfen(desired):
    max_num = desired * 8
    n = 2
    lst = list(range(max_num + 1))
    lst[1] = 0
    while n < max_num:
        if lst[n] != 0:
            m = n * 2
            while m < max_num:
                lst[m] = 0
                m += n
        n += 1
    lst2 = []
    for i in lst:
        if lst[i] != 0:
            lst2.append(lst[i])
    del lst

    return lst2[desired - 1]


DESIRED = int(input('Ведите какое по счету простое число требуется найти '))
if DESIRED <= 1000:
    print(f'Простое число под номером {DESIRED} это: {simple_number_list(DESIRED)}')
    print(f'Простое число под номером  {DESIRED} это: {sieve_eratosfen(DESIRED)}')
    print(timeit.timeit('simple_number_list(DESIRED)',
                    setup='from __main__ import simple_number_list, DESIRED', number=1000))
    print(timeit.timeit('sieve_eratosfen(DESIRED)',
                    setup='from __main__ import sieve_eratosfen, DESIRED', number=1000))
else:
    print(f'Число {DESIRED} слишком велико')

"""Ввел намереное ограничение лимита вводимого числа,
чтобы оно не превышало возможное максимальное число в ряду чисел
в ином случае в функции с решетом создавался огромный список лишних чисел,
что тормозило расчеты в разы на функции с ним,
теперь же решето уже после 400 значения начинает работать быстрее алгоритма без решета
"""
