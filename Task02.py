# Задача 2: Найдите сумму цифр трехзначного числа.

number = input ("Введите трехзначное число: ")

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Ошибка. Введено не число!")
        number = input ("Введите повторно число: ")

if number>99 and number<1000:
    summa = number//100 + number%10 + (number//10)%10
    print ("Сложение цифр в числе = {0}" .format(summa))
else:
    print ("Введено не трехзначное число!")