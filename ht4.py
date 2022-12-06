# Задача 1.Вычислить число Пи c заданной точностью d 

import os
os.system('cls||clear')
import math
d_inp = input('Задайте точность, например 0.001: ').split('.')
pi = str(math.pi).split('.')
d_pi = len(d_inp[1])
pi_1 = pi[0]+'.'
pi_2 = pi[1]
print(f'пи c точностью {float(pi_1 + pi_2[:d_pi])}')

# Задача 2. Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

import os
os.system('cls||clear')
def count_i(i):
    count = 0
    for j in range(2,i-1):
        if i%j==0:
            count=count+1
    return count

N = int(input('Введите N: '))

for i in range(2,N+1):
    if (N % i == 0) and (count_i(i) < 1):
        print(i)

# Задача 3. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

import os
os.system('cls||clear')
numbers_list = [1, 4, 5, 6, 6, 3, 4, 2]
print(f'исходный список {numbers_list}')
uniknumbers_list = list(set(numbers_list))
print(f'результат {uniknumbers_list}')

# Задача 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.(записать в строку)

import os
os.system('cls||clear')
import random

k = int(input('Введите степень K: '))

def polinom_s(k):
    listk = []
    for i in range(k+1):
        i = random.randrange(0, 101)
        listk.append(i)
    return listk

polinom = []
polinoms = polinom_s(k)
print(f'крэффициенты: {polinoms}')
s = k
for i in range(0,(len(polinoms))):
    polinom.append(str(polinoms[i])+'*x**'+str(s))
    s=s-1
pol_str = '+'.join(polinom)
with open('filep.txt', 'w') as pol:
    pol.write(pol_str)


#Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.В file1.txt : 2*x**2 + 4*x + 5 
# # В file2.txt: 4*x**2 + 1*x + 4 Результирующий файл:6*x**2 + 5*x + 9

import os
os.system('cls||clear')
with open('file1.txt','r') as f1:
    mnog1 = f1.read() + '+'
print(f'позиции из файла: {mnog1}')with open('file2.txt','r') as f2:
    mnog2 = f2.read()
print(f'позиции из файла: {mnog2}')
import sympy
x = sympy.Symbol('x')
with open('file3.txt', 'w') as f3:
        f3.write(str(sympy.simplify(mnog1+mnog2)))