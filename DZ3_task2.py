# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint
n=int(input('Введите длину списка: '))
list=[randint(1,9) for i in range (n)]
result_list=[]

for i in range(n//2):
    result_list.append(list[i]*list[len(list)-i-1])
if n%2==1:
    result_list.append(list[n//2] ** 2)
print (f'{list} => {result_list}')
