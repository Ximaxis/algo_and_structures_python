"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

COUNT_NUMBER = int(input('Введите количество чисел которые будем проверять: '))
FIND = int(input('Введите цифру которую ищем: '))

def search(n, f, i = 0):
    if n < 1:
        return i
    else:
        if n % 10 == f:
            i += 1
        else:
            pass
    return search((n // 10), f, i)

def count_number(c, f, i = 0):
    if c == 0:
        return i
    else:
        number = int(input(f'Введите {c} число которые будем проверять: '))
        i += search(number, f)
        return count_number(c - 1, f, i)

print(f"В заданой последоватеельности цифра {FIND} встраечается {count_number(COUNT_NUMBER, FIND)} раз")

""" 
Решение циклом

count_number = int(input('Введите количество искомых чисел: '))
find = int(input('Введите число которое ищем: '))
count = 0
while count_number != 0:
    number = input('Введите число: ')
    count_number -= 1
    for i in number:
        if int(i) == find:
            count += 1

print("Число %d нашлось %d раз(а)" % (find, count))
"""
