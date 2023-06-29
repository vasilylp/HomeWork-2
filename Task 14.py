"""Задача 14: ___________________________________________________________
Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N."""

N = int(input("Введите целое число : "))
listDegrees =[]
degree = 0
for n in range(N):
    degree = 2 ** n
    if degree < N:
        listDegrees.append(degree)
print(listDegrees)
