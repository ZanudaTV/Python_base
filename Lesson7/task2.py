# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают
# число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два
# аргумента, как, например, у операции умножения.
# Ввод:
#
# print_operation_table(lambda x, y: x * y)


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             print(operation(i, j), end='\t')
#         print()
#
#     # print([i * j for i in range(1, num_rows + 1) for j in range(1, num_columns + 1)])
#
#
#
#
# print_operation_table(lambda x, y: x * y, int(input('колличество строк = ')), int(input('колличество столбцов = ')))

numWatermelon = int(input('Enter the number of watermelons: '))
massWatemelons = [int(input('Enter the mass of watermelons through ')) for value in range(numWatermelon)]
maxMass = massWatemelons[0]
minMass = massWatemelons[0]
print(massWatemelons)
for i in massWatemelons:
    if i > maxMass:
        maxMass = i
    if i < minMass:
        minMass = i
print('Minimum weight =', minMass)
print('Maximum weight =', maxMass)