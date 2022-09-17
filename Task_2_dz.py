# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]

def mult(num):
    res = []
    while len(num) > 1:
        res.append(num[0]*num[-1])
        del num[0] 
        del num[-1] 
    if len(num) == 1: 
        res.append(num[0]**2)       
    return res

print(mult(list1))
print(mult(list2))