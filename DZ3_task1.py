# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
n=int(input('Введите длину списка: '))
list=[randint(0,9) for i in range (n)]
sum=0
biutyList=''
for i in range(1,n,2):
    sum+=list[i]
    if ((i==(n-1) or i==(n-2)) and n>3):
        biutyList+=f' и {list[i]}'
    elif (i==1):
        biutyList += f'{list[i]}'
    elif ((i==(n-1) or i==(n-2)) and n<3):
        biutyList+=f'{list[i]}'
    else:
        biutyList += f', {list[i]}'
if (n<2):
    print(f'{list} -> отсутсвуют нечетные позиции')
elif (n<4):
    print(f'{list} -> на нечётной позиции элемент {biutyList}, ответ: {sum}')
else:
    print(f'{list} -> на нечётных позициях элементы {biutyList}, ответ: {sum}')



