# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

def workSpisok (array):
    massiv = []
    for i in range(len(array)//2):
        massiv.append(array[i]*array[-i-1])
    if len(array)%2 != 0:
        massiv.append (array[len(array)//2]**2)
    return massiv

size = input("Введите размер списка: ")

while type(size) != int:
    try:
        size = int(size)
    except ValueError:
        print ("Ошибка. Введено не число!")
        size = input("Введите повторно размер массива: ")

spisok=[]
for i in range(size):
    spisok.append(randint(0,10))

print (spisok)

result = workSpisok(spisok)
print(result)