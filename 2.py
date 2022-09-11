# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

some_list = [input() for _ in range(int(input('Введите количество элементов: ')))]
print(f'some_list = {some_list}')
length = math.ceil(len(some_list)/2)
new_list = [0 for _ in range(int(length))]
tempStart = 0
tempEnd = len(some_list) - 1
for i in range(0, len(new_list)):
        new_list[i] = int(some_list[tempStart]) * int(some_list[tempEnd])
        tempStart += 1
        tempEnd -= 1
print(f'new_list = {new_list}')


