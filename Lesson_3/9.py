""" 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

from random import random

M = 10
N = 10
A = []
MX = 0
print("В матрице")
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 100)
        b.append(n)
        print(f"{n}\t ", end="")
    A.append(b)
    print()

for j in range(M):
    mn = 200
    for i in range(N):
        if A[i][j] < mn:
            mn = A[i][j]
    if mn > MX:
        MX = mn
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {MX}")
