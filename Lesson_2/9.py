"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def max_summa(MAX_SUM = 0, MAX_NUMB = 0):
    NUMBER = int(input('Введите число: '))
    if NUMBER == 0:
        return print(f"Максимально веденвое число - {MAX_NUMB} "
                     f"\n сумма его цифр - {MAX_SUM}")
    else:
        if summa(NUMBER) > MAX_SUM:
            MAX_SUM = summa(NUMBER)
            MAX_NUMB = NUMBER
    return max_summa(MAX_SUM,MAX_NUMB)

def summa(N, S = 0):
    if N < 1:
        return S
    else:
        S += (N % 10)
    return summa((N // 10), S)

max_summa()

"""
Решение циклом

print("0 - вывод итогов")
MAX_SUM = 0
MAX_NUMB = 0

while True:
    NUMBER = input('Введите число: ')
    if NUMBER != '0':
        SUMMA = 0
        for i in NUMBER:
            SUMMA += int(i)
            if SUMMA > MAX_SUM:
                MAX_SUM = SUMMA
                MAX_NUMB = NUMBER
    else:
        break

print('Максимально веденвое число - %s, сумма его цифр - %d' % (MAX_NUMB, MAX_SUM))
"""
