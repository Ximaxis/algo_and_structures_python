""" 3.	По введенным пользователем координатам двух точек
вывести уравнение прямой вида y = kx + b, проходящей через эти точки. """

X1 = float(input("Введите координату x точки 1 = "))
Y1 = float(input("Введите координату y точки 1 = "))
X2 = float(input("Введите координату x точки 2 = "))
Y2 = float(input("Введите координату y точки 2 = "))

K = (Y1 - Y2) / (X1 - X2)
B = Y2 - K * X2
print("Уравнение прямой:")
print(" y = %.2f*x + %.2f" % (K, B))
