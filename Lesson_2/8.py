"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


NUMBER = int(input('Введите число: '))
FIND = int(input('Введите цифру которую ищем: '))

def search(N, F, I = 0):
    if N < 1:
        return I
    else:
        if N % 10 == F:
            I += 1
        else:
            pass
    return search((N // 10), F, I)

print(f"В числе {NUMBER} цифра {FIND} встраечается {search(NUMBER,FIND)} раз")

""" 
Решение циклом

number = input('Введите число: ')
find = int(input('Введите число которое ищем: '))
count = 0
for i in number:
    if int(i) == find:
        count += 1

print("Число %d нашлось %d раз(а)" % (find, count))

"""
