""" 3.	В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы."""

from random import random
N = 20
A = [0]*N
for i in range(N):
    A[i] = int(random() * 100)

B = A
LOW = min(B)
HIGH = max(B)
IL = B.index(LOW)
IH = B.index(HIGH)
B[IL], B[IH] = B[IH], B[IL]
print(f"В массиве {A} "
      f"\n минимальный и максимальный элемент имеют индексы {IL, IH}"
      f"\n меняем их местами и получаем измененный массив"
      f"\n {B}")
