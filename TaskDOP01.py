# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

from random import randint

def summaNegative (array):
    summa = 0
    count=0
    for i in range(len(array)):
        if array[i]<0:
            summa += array[i]
            count +=1
    return (summa, count)

size = input("Введите размер списка: ")

while type(size) != int:
    try:
        size = int(size)
    except ValueError:
        print("Введи число, Дурачок!")
        size = input("Повторная попытка")

spisok = []

for i in range(size):
    spisok.append(randint(-100, 100))

print(spisok)

result, count = summaNegative(spisok)
print("В списке {0} отрицательных элементов. Их сумма равна {1}" .format(count, result))