#Задайте число. Составьте список чисел Фибоначчи, 
#в том числе для отрицательных индексов.

#Пример:

#    - для k = 8 список будет выглядеть так: 
#    [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

num = int(input("Введите число: "))
if num < 0: 
    n = num*-1
f1 = f2 = 1
list1 = [f1, f2]
for i in range(2, num):
    f1,f2 = f2, f1 + f2
    list1.append(f2)
print(list1)
f1=f2=1
for i in range(-num, 1):
    f1,f2 = f2, f1 - f2
    list1.insert(0, f2)
print(list1)
