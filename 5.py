# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
import math
fib_list = [0 for _ in range(int(input('Введите k: ')) * 2 + 1)]
count = math.ceil(len(fib_list)/2)
fib_list[count] = 1

for i in range(count, len(fib_list)):
    fib_list[i] += fib_list[i - 1] + fib_list[i - 2]
for i in range(0, count - 1):
    if i%2 != 0:
        fib_list[math.ceil(len(fib_list)/2) - 2 - i] = - fib_list[count]
        count += 1
    else:
        fib_list[math.ceil(len(fib_list) / 2) - 2 - i] = fib_list[count]
        count += 1
print(fib_list)