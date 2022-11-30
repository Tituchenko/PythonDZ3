# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

numberDec=int(input('Введите десятичное число: '))
temp=numberDec
boolNumber=''
while (temp!=0):
    boolNumber+=str(temp%2)
    temp=temp//2
boolNumber=boolNumber[::-1]
print (f'{numberDec} - > {boolNumber}')

