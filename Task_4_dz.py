# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))

def convert(n):
    num = ''
    while n >= 1:
        num += str(n % 2)
        n = n // 2
    return num[::-1]

print(convert(n))
