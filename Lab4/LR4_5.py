import math
a = int(input("Введите 1 сторону параллелепипеда (ширина): "))
b = int(input("Введите 2 сторону параллелепипеда (длина): "))
c = int(input("Введите 3 сторону параллелепипеда (высота): "))
V = a*b*c
S_bok = 2*(a*c + b*c)
print("Объём параллелепипеда равен: ",V)
print ("Боковая площадь параллелепипеда равна: ",S_bok)