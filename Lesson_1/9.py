""" 9.Вводятся три разных числа.
Найти, какое из них является средним
(больше одного, но меньше другого). """

A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
C = int(input('Введите третье число: '))

if (A > B > C) or (A < B < C):
    print("Средним числом является " + str(B))
elif (C > A > B) or (C < A < B):
    print("Средним числом является " + str(A))
else:
    print("Средним числом является " + str(C))
