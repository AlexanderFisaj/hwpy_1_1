# Задача 4. Напишите программу, которая на вход принимает число (N), 
# а на выходе показывает все чётные числа от 1 до N.

number = int(input('Введите число: '))
count = 2
while number < 0:
    number = int(input('Число не должно быть отрицательным.\nПовторите ввод: '))
if number == 1:
    print('Четных чисел нет.')
else:
    while count <= number:
        print(count, end=' ')
        count += 2