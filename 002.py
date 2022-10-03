# Задача№2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# print('Введите целое число: ')
# N = int(input())
# list = []
# fact = 1
# for i in range(1, N + 1):
#     fact *= i
#     list.append(fact)
# print(list)

# Решение через функцию

# print('Введите целое число: ')
# N = int(input())
# def fac(x):
#     if x == 0:
#         return 1
#     else:
#         return x * fac(x -1)
# print(fac(N))