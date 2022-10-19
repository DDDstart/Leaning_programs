# Логические операции, операции сравнения
a = int(input()) # Проверка того, что ввдеденное число положительное
print(a > 0)
a = int(input()) # Проверка того, что ввдеденное число двузначное
print(10 <= a < 100)
a = int(input()) # Проверка того, что ввдеденное число двузначное 'and'
print(a >= 10 and a < 100)
x1, x2, x3 = False, True, False # Результат 'True'
print(not x1 or x2 and x3)
x1, x2, x3 = False, True, False # Результат 'False'
print(((not x1) or x2) and x3)
#
# Расставьте скобки в выражении (a and b or not a and not b)
# в соответствии с порядком вычисления выражения (приоритетом операций)
# (a and b or not a and not b) == (3 * 2 + -3 * -2)
# Ответ: ((a and b) or ((not a) and (not b)))
#
# Выполните код в интерпретаторе Python 3
# x = 5
# y = 10
# y > x * x or y >= 2 * x and x < y
x = 5
y = 10
print(((y > (x * x)) or ((y >= (2 * x)) and (x < y)))) # Ответ 'True'
#
# Найдите результат выражения для заданных значений a и b
# a and b or not a and not b
a =  True
b = False
print(a and b or not a and not b) # Ответ 'False'