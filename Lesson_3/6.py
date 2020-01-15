"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random
N = 20
A = [0]*N
for i in range(N):
    A[i] = int(random() * 100)

LI = 0
HI = 0
for i in range(1, N):
    if A[i] < A[LI]:
        LI = i
    elif A[i] > A[HI]:
        HI = i

if LI > HI:
    LI, HI = HI, LI

S = 0
for i in range(LI+1, HI):
    S += A[i]

print(f"В массиве {A} \nсумма чисел между числами {A[LI], A[HI]} равна {S}")
