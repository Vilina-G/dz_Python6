print("""Задача 30.
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
an = a1 + (n-1) * d. Каждое число вводится с новой строки.""")

# first_element = (input('Введите первый элемент: '))
# element_diff = int(input('Введите разность между элементами: '))
# quantity_elements = int(input('Введите количество элементов: '))
#
#
#
# def arithmetic_sequence(first_element: int, element_diff: int, quantity_elements: int):
#     sequence = [first_element]
#     for i in range(2, quantity_elements + 1):
#         sequence.append(first_element + (i - 1) * element_diff)
#     return sequence
# print(*arithmetic_sequence(first_element, element_diff, quantity_elements))

 print("""Задача 32.
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума) """)


# def create_list(x: int):
#     my_list = []
#     for _ in range(x):
#         my_list.append(int(input('Введите число: ')))
#     return my_list
#
# num_list = create_list(int(input('Введите размер массива: ')))
# left_endpoint = int(input('Введите MIN диапазона: '))
# right_endpoint = int(input('Введите MAX диапазона: '))
#
# def indexes_of_numbers(num_list: list, start: int, end: int):
#     indexes_list = []
#     for i in range(len(num_list)):
#         if start <= num_list[i] <= end:
#             indexes_list.append(i)
#     return indexes_list
#
# print(*num_list)
# print(*indexes_of_numbers(num_list, left_endpoint, right_endpoint))
