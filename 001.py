# Задача№1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# num = float(input('Введите вещественное число: '))
# num_abs = abs(num)
# result = 0
# for i in 1, 2, 3, 4, 5:
#     result += num_abs % 10

# print(result)

num = input('Введите вещественное число: ')
result = 0
for i in num:
    if i != '.':
        result += int(i)
print(result)