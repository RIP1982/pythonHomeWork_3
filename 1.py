# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

some_list = [input() for _ in range(int(input('Введите количество элементов: ')))]
summa = 0
for i in range(0, len(some_list)):
    if i%2 != 0:
        summa += int(some_list[i])
        print(i)
print(some_list)
print(summa)
