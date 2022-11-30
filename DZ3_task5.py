# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k=int(input('Введите k: '))

fibi=[]
fibi.insert(0,1)
fibi.insert(0,-1)
for i in range (0,k+1):
    fibi.append(fibi[len(fibi)-1]+fibi[len(fibi)-2])
    if i>2:
        fibi.insert (0,fibi[1]-fibi[0])
print (f'{fibi}')
