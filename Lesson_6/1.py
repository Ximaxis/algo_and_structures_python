"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from math import sqrt
from memory_profiler import profile
from pympler import asizeof
from guppy import hpy
h = hpy()

# Первый алгоритм
@profile
def simple_number_list(desired):
    n = desired * 2 * round(sqrt(sqrt(desired)))
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


print(h.heap())
h = hpy()
# Второй алгоритм
@profile
def sieve_eratosfen(desired):
    max_num = desired * 2 * round(sqrt(sqrt(desired)))
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


print(h.heap())
DESIRED = int(input('Ведите какое по счету простое число требуется найти '))
print(asizeof.asizeof(simple_number_list(DESIRED)))
print(asizeof.asizeof(sieve_eratosfen(DESIRED)))

"""
Версия Python 3.7 OS Windows 10 разрядность 64-bit
Ниже приведены результаты замеров, если их рассмотреть то видно следующее:
Функция hpy нам показывает что самое большое количество памяти выделяется на данные типа str
по оценочному выделению памяти первый алгоритм чуть более затратный
Total size = 4229376 bytes. Total size = 4228854 bytes.

Функция asizeof выдает одинаковые значения
16 == 16

Для большей наглядности входные данные для алгоритмов установил на значение 10000
и функция profile показывает что в 1 алгоритме изначально выделеного объема памяти 
хватает, только на формировании списка требуется немного дополнительной
Для второго алгоритма мы видим что на формирование списка чисел был выделен
солидный объем дополнительной памяти, а так же видно что после переноса всех чисел
отличных от нуля во второй список и удаление первого списка часть памяти была освобождено


Partition of a set of 60800 objects. Total size = 4229376 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  17397  29  1222281  29   1222281  29 str
     1  15644  26   642624  15   1864905  44 tuple
     2   7925  13   442611  10   2307516  55 bytes
     3   4009   7   337776   8   2645292  63 types.CodeType
     4   3914   6   281808   7   2927100  69 function
     5    642   1   261132   6   3188232  75 type
     6    642   1   198120   5   3386352  80 dict of type
     7    155   0   153096   4   3539448  84 dict of module
     8    492   1   119328   3   3658776  87 dict (no owner)
     9   1271   2    55924   1   3714700  88 types.WrapperDescriptorType
<190 more rows. Type e.g. '_.more' to view.>
Partition of a set of 60761 objects. Total size = 4228854 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  17397  29  1222281  29   1222281  29 str
     1  15645  26   642668  15   1864949  44 tuple
     2   7925  13   442611  10   2307560  55 bytes
     3   4009   7   337776   8   2645336  63 types.CodeType
     4   3916   6   281952   7   2927288  69 function
     5    642   1   261132   6   3188420  75 type
     6    642   1   198120   5   3386540  80 dict of type
     7    155   0   153096   4   3539636  84 dict of module
     8    493   1   119464   3   3659100  87 dict (no owner)
     9   1271   2    55924   1   3715024  88 types.WrapperDescriptorType
<190 more rows. Type e.g. '_.more' to view.>

Ведите какое по счету простое число требуется найти 10000

Line #    Mem usage    Increment   Line Contents
================================================
    17     18.4 MiB     18.4 MiB   @profile
    18                             def simple_number_list(desired):
    19     18.4 MiB      0.0 MiB       n = desired * 2 * round(sqrt(sqrt(desired)))
    20     18.4 MiB      0.0 MiB       lst = [2]
    21     18.6 MiB      0.1 MiB       for i in range(3, n + 1, 2):
    22     18.6 MiB      0.0 MiB           if (i > 10) and (i % 10 == 5):
    23     18.6 MiB      0.0 MiB               continue
    24     18.6 MiB      0.0 MiB           for j in lst:
    25     18.6 MiB      0.0 MiB               if j * j - 1 > i:
    26     18.6 MiB      0.0 MiB                   if len(lst) == desired:
    27     18.5 MiB      0.0 MiB                       return lst[desired - 1]
    28                                             else:
    29     18.6 MiB      0.0 MiB                       lst.append(i)
    30     18.6 MiB      0.0 MiB                   break
    31     18.6 MiB      0.0 MiB               if i % j == 0:
    32     18.6 MiB      0.0 MiB                   break
    33                                     else:
    34     18.4 MiB      0.0 MiB               lst.append(i)


16

Line #    Mem usage    Increment   Line Contents
================================================
    37     18.6 MiB     18.6 MiB   @profile
    38                             def sieve_eratosfen(desired):
    39     18.6 MiB      0.0 MiB       max_num = desired * 2 * round(sqrt(sqrt(desired)))
    40     18.6 MiB      0.0 MiB       n = 2
    41     22.3 MiB      3.7 MiB       lst = list(range(max_num + 1))
    42     22.3 MiB      0.0 MiB       lst[1] = 0
    43     22.3 MiB      0.0 MiB       while n < max_num:
    44     22.3 MiB      0.0 MiB           if lst[n] != 0:
    45     22.3 MiB      0.0 MiB               m = n * 2
    46     22.3 MiB      0.0 MiB               while m < max_num:
    47     22.3 MiB      0.0 MiB                   lst[m] = 0
    48     22.3 MiB      0.0 MiB                   m += n
    49     22.3 MiB      0.0 MiB           n += 1
    50     22.2 MiB      0.0 MiB       lst2 = []
    51     22.2 MiB      0.0 MiB       for i in lst:
    52     22.2 MiB      0.0 MiB           if lst[i] != 0:
    53     22.2 MiB      0.0 MiB               lst2.append(lst[i])
    54     21.4 MiB      0.0 MiB       del lst
    55                             
    56     21.4 MiB      0.0 MiB       return lst2[desired - 1]


16
"""
