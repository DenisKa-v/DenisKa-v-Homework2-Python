# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2

# count0 = 0
# count1 = 0
# n = int(input('Введите количество монет '))
# print('Введите одно из двух значени: 1 - если решка, 0 - если орел')
# for _ in range(n):
#     temp = int(input())
#     if temp == 1:
#         count1 += 1
#     else:
#         count0 += 1
# if count1 >= count0:
#     print(f'Минимальное количество монет, которые нужно перевернуть, равно {count0}.')
# else:
#     print(f'Минимальное количество монет, которые нужно перевернуть, равно {count1}.')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3

# s, p = ((int(input('Назовите сначала сумму, а следом произведение двух натуральных чисел ')) for _ in range(2)))
# for x in range(1, s):
#     y = s - x
#     if x <= y and x * y == p:
#         print(f'Задуманные натуральные числа x = {x}, y = {y}')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# N = float(input('Введите число: '))
# n = 1
# print('Целые степени двойки:')
# while n <= N:
#     print(n, end=' ')
#     n = n * 2
