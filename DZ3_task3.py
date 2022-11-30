# элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import Decimal
from random import randint
n=int(input('Введите длину списка: '))
maxFloat=5 #Максимальное число цифр после запятой
myList=n*[None]
maxFloatPart=0
minFloatPart=0
for i in range(n):
    curFloat=Decimal (randint(0,maxFloat)) # случайное количество цифр после запятой
    myList [i]=Decimal (randint(0,10) + randint(0,10 ** curFloat)/(10 ** (curFloat)))
    floatPart=myList [i]-int(myList [i])
    if floatPart!=0:
        if floatPart>maxFloatPart or maxFloatPart==0:
                maxFloatPart=floatPart
        if floatPart < minFloatPart or minFloatPart==0:
                minFloatPart = floatPart

    myList=[str(val) for val in myList] #Уберем из вывода слово Deciaml
print (f'{myList} => {maxFloatPart-minFloatPart}')


