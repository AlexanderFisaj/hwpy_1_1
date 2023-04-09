# Задача1. 
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и выводит название этого дня недели.

numDey = int(input('Введите цифру дня недели: '))
if numDey > 7: print('Нет такого дня')
elif numDey == 1: print('Понедельник')
elif numDey == 2: print('Вторник')
elif numDey == 3: print('Среда')
elif numDey == 4: print('Четверг')
elif numDey == 5: print('Пятница')
elif numDey == 6: print('Суббота')
elif numDey == 7: print('Воскресенье')