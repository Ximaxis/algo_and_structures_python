"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
number = int(input("Введите натуральное число "))

def func(n, even = 0, odd = 0):
    if n < 1:
        return print(f"Четных чисел: {even} нечетных: {odd}")
    else:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        return func((n // 10), even, odd)

func(number)

"""
Вариант в цикле 1

number = int(input())
even=odd=0
while n>0:
    if n%2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print(f"Четных чисел: {even} нечетных: {odd}")

Вариант в цикле 2

number = int(input())
even = 0
odd = 0
for i in number:
    if (int(i) % 2 == 0):
        even += 1
    else:
        odd += 1
print(f"Четных чисел: {even} нечетных: {odd}")
"""
