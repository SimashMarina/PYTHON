# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_1 = [1.1, 1.2, 3.1, 5, 10.01]

def find_diff(num):
    nums = [round(x - int(x), 2) for x in (num)]  # Не совсем правильное решение, так как округляет.
    return max(nums) - min(nums)

print (list_1)
print(find_diff(list_1))