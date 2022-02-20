

"""Цикл for функция range"""
numbers = 1, 2, 3, 4
#
# for i  in numbers:
#     print(i)




# start = int(input("Введите начальное число последовательности:"))
# stop = int(input("Введите конечное число послдеовательности:"))
#
# quantity = 0
# sum_of_numbers = 0
#
# for number in range(start, stop):
#     sum_of_numbers += number
#     quantity = 2
#
# print(f'Сумма положительных чисел: {pol}')
# print(f'Сумма отрицательных чител: {otr}')

# number_of_string = 0
#
#   for i in range(1, 6):
#       print(f'Строка')

# n = int(input('Введите число '))
#
# for i in range(1, n+1):
#     if i == 1:
#         print('Красный')
#     if i == 2:
#         print('Оранжевый')
#     if i == 3:
#         print('Желтый')
#     if i == 4:
#         print('Зеленый')
#     if i == 5:
#         print('Голубой')
#     if i == 6:
#         print('Синий')
#     if i == 7:
#         print('Фиолетовый')
#
#     if n > 7 or n < 1:
#         print('В радуге только 7 цветов')

n = int(input('Введите n: '))
for i in range(1, 11):
    print(f'{n} * {i} = {n*i}')
