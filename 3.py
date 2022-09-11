# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
some_list = [float(input()) for _ in range(int(input('Введите количество элементов: ')))]
print(f'some_list = {some_list}')
new_list = [0 for _ in range(0, len(some_list))]
for i in range(0, len(some_list)):
    new_list[i] = round(some_list[i] - int(some_list[i]), 2)
print(f'new_list[max] - new_list[min] = {max(new_list) - min(new_list)}')


